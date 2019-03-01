#! python3
# Compare the numbers of object entries.

import csv
import sys

assert len(sys.argv) != 0, 'Enter file name as an argument'
file_path = sys.argv[1]
raw_file = open(file_path, newline='')
csv_reader = csv.reader(raw_file)
res_file = open(file_path.rstrip('.csv') + '_next_merge.csv', 'w', newline='')
csv_writer = csv.writer(res_file)

for row in csv_reader:
    if csv_reader.line_num == 1:
        csv_writer.writerow(row)
        continue
    master_num = int(row[2])
    servant_num = int(row[3])
    if master_num < servant_num:
        csv_writer.writerow(row)
        print('Found value: Master #%d, Servant #%d' % (master_num, servant_num))

raw_file.close()
res_file.close()
