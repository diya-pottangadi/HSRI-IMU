import csv
import glob

input_glob = 'chest/raw data/dataLog0000*.TXT'
data_csv = 'chest_all_data.csv'

with open(data_csv, 'w', newline='') as out_f:
    writer = csv.writer(out_f)
    first = True
    
    for name in glob.glob(input_glob):
        with open(name, newline='') as in_f:
            reader = csv.reader(in_f)
            header = next(reader)
            if first:
                writer.writerow(header)  
                first = False
            for row in reader:
                writer.writerow(row)