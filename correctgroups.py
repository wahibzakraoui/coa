from asyncore import write
import csv
""" with open('data.csv') as csv_file, open("out_file.csv", 'w') as f_out:
        
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    
    for cur_line in csv_reader:
        try:
            write = csv.writer(f_out)
            codelength = int(cur_line[1])
            next_line = next(csv_reader)
            if cur_line[2] == next_line[2][0:codelength]:
                cur_line[6] = 1
                
            else:
                cur_line[6] = 0
            write.writerow(cur_line)
            write.writerow(next_line)
        except:
            pass """
def getrow(row):
    row[len(row)-1] = row[len(row)-1].rstrip()
    return row

def load_from_csv(filename):
    with open(filename,'r', encoding='utf-8-sig') as csvfile:
        return [getrow(row) for row in csv.reader(csvfile, delimiter=',')]

rows = load_from_csv('data.csv')
length = len(rows)

for key, curline in enumerate(rows):
    codelength = int(curline[1])
    if key < length-1:
        nextrow = rows[key+1]
        code = int(curline[2])
        nextcode = int(nextrow[2][0:codelength])
        
        if code == nextcode :
            curline[6] = '1'
        else:
            curline[6] = '0'

        """ write = csv.writer(outfile)
        write.writerow(curline) """

with open("out_file.csv", "a+", encoding='utf-8-sig') as outfile:
    write = csv.writer(outfile)
    write.writerows(rows)