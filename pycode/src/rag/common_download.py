import time
import csv
from odps import ODPS

endpoint = "http://service-corp.odps.aliyun-inc.com/api"
access_id = "WXmp7aYLxzMRZpsz"
access_key = "FzMCu7B03VGimtMYxfI6Jx9FO3QoDr"
project_name = "b2b_crm_dev"
table_name = "url_user_agg_high_qpm"
file_name = '/Users/quandaling/Desktop/url_user_agg_high_qpm.csv'

odps_instance = ODPS(
    endpoint=endpoint,
    access_id=access_id,
    secret_access_key=access_key,
    project=project_name
)

if __name__ == '__main__':
    table = odps_instance.get_table(name=table_name, project=project_name)
    total_write = 0
    with open(file_name, 'w+', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        with table.open_reader(partition=None) as reader:
            total = reader.count
            print(f"{table_name}, total:{total}")
            head_info = []
            for head in table.table_schema.columns:
                head_info.append(head.name)
            csv_writer.writerow(head_info)
            page_size = 1000
            start = 0
            while start < total:
                start_time = time.time()
                end = start + page_size
                item_list = []
                print(f"from {start} to {end}")
                for row in reader[start:end]:
                    csv_writer.writerow(row.values)
                    total_write += 1
                end_time = time.time()
                print(f"{total_write}/{total}, cost:{end_time - start_time}")
                start += page_size
