from datetime import datetime, timedelta
import happybase

def upload_logs_to_hbase(file_path, table_name):
    connection = happybase.Connection('localhost')
    table = connection.table(table_name)

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(' ')
            timestamp = parts[0] + ' ' + parts[1]
            method = parts[2]
            endpoint = parts[3]
            status_code = parts[4]
            row_key = f"{timestamp}_{method}_{endpoint}"

            table.put(row_key, {
                'cf:timestamp': timestamp,
                'cf:method': method,
                'cf:endpoint': endpoint,
                'cf:status_code': status_code,
                'cf:data': line
            })

def query_logs_for_hour(table_name, query_hour):
    connection = happybase.Connection('localhost')
    table = connection.table(table_name)

    start_time = datetime.strptime(query_hour, '%Y-%m-%dT%H:00:00')
    end_time = start_time + timedelta(hours=1)

    count = 0
    for key, data in table.scan():
        row_timestamp = data[b'cf:timestamp'].decode('utf-8')
        try:
            log_time = datetime.strptime(row_timestamp, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            log_time = datetime.strptime(row_timestamp, '%Y-%m-%d')

        if start_time <= log_time < end_time:
            count += 1

    return count

if __name__ == "__main__":
    hour = '2024-05-31T23:00:00'
    request_count = query_logs_for_hour('logtaable', hour)
    print(f"Number of requests in the selected hour: {request_count}")
