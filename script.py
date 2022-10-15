import json
import csv
# if code is c and code length is n, look for all items with code[0:n] = c and length = n+1
def walk_roots(i):

    with open('data.csv') as csv_file:
        
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            classcode = int(row[0])
            codelength = int(row[1])
            code = int(row[2])
            account = row[3].strip()
            try:
                #roots
                if codelength == 1 and classcode == i:
                    account_name = str(code) + ' - ' + account
                    #roots.update({account_name : {'account_number' : code, 'is_root': 1, 'is_group': 1}})
                    roots[account_name] = {'account_number' : code, 'is_root': 1, 'is_group': 1}
                    #roots[account_name]['account_number'] = code
                    
                """ # x level
                if codelength > 1 and classcode == i and code[0:codelength] == code and codelength == len(root) + 1:
                    pass """
            except:
                #print(row)
                pass

def walk_nodes(i):
    for rootkey, root in roots.items(): 
        with open('data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                classcode = int(row[0])
                codelength = int(row[1])
                code = int(row[2])
                account = row[3].strip()
                node_key = root['account_number']
                
                try:
                    """ if codelength == 2 and classcode == i :
                        print(row[2][0:codelength-1], root['account_number'], codelength, len(str(root['account_number']))) """
                    if codelength > 1 and classcode == i and row[2][0:codelength-1] == str(node_key) and codelength == len(str(node_key)) + 1:
                        #print(row)
                        roots[rootkey].update({account: {'account_number': code}})
                        pass
                except:
                    pass

def walk_nodes_indexed(i):
    
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            classcode = int(row[0])
            codelength = int(row[1])
            code = int(row[2])
            account = row[3].strip()
            for rootkey, root in roots.items(): 
                if classcode != int(root['account_number']):
                    continue
                if codelength == 1:
                    continue
                try:
                    if int(row[2][0:codelength-1]) == int(root['account_number']):
                        print(root)
                        pass
                except:
                    print(row[2])




data = []
roots = dict()


for i in range(1, 8):
    walk_roots(i)
    walk_nodes_indexed(i)
    #print(len(roots.items()))
with open("sample.json", "w") as outfile:
    #json.dump(roots, outfile)
    pass