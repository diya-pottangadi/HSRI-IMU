import csv
from datetime import datetime, time

INPUT_CSV  = 'left hand/left_hand_all_data.csv'
OUTPUT_CSV = 'left_hand_picking_up_item.csv'

# time window for action: picking up glass of water from surface, bringing it to mouth, setting it down on a surface
START = time(12, 27, 30)
END   = time(12, 27, 38)

with open(INPUT_CSV, newline='') as infile, open(OUTPUT_CSV, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    
    for row in reader:
        t = datetime.strptime(row['rtcTime'], '%H:%M:%S.%f').time()
        
        if START <= t <= END:
            writer.writerow(row)
