import json
import csv
from path_dict import PathDict
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
            is_group = int(row[6].strip()) if row[6].strip() != '' else 0
            try:
                #roots
                if codelength == 1 and classcode == i:
                    account_name = str(code) + ' - ' + account
                    #roots.update({account_name : {'account_number' : code, 'is_root': 1, 'is_group': 1}})
                    if  row[4].strip() != '':
                        roots[account_name] = {'account_number' : code, 'root_type':  row[4].strip(), 'is_group': is_group}
                    else:
                        roots[account_name] = {'account_number' : code, 'is_group': is_group}
                    #roots[account_name]['account_number'] = code
                    
                """ # x level
                if codelength > 1 and classcode == i and code[0:codelength] == code and codelength == len(root) + 1:
                    pass """
            except:
                #print(row)
                pass

def walk_nodes():
    for depth in range(2,6):
        db = PathDict(roots)
        if depth == 2:
            with open('data.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                next(csv_reader)
                for row in csv_reader:
                    classcode = int(row[0])
                    codelength = int(row[1])
                    code = int(row[2])
                    account = row[3].strip()
                    is_group = int(row[6].strip()) if row[6].strip() != '' else 0
                    if codelength != depth:
                        continue
                    for rootkey, root in roots.items():
                        if isinstance(root, dict) and root['account_number'] == int(row[2][0:codelength-1]):
                            if  row[5].strip() == '':
                                roots[rootkey].update({account: {'account_number': code, 'is_group' : is_group}})
                            else:
                                roots[rootkey].update({account: {'account_type': row[5].strip(),'account_number': code, 'is_group' : is_group}})

        if depth == 3:
            with open('data.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                next(csv_reader)
                for row in csv_reader:
                    classcode = int(row[0])
                    codelength = int(row[1])
                    code = int(row[2])
                    account = row[3].strip()
                    is_group = int(row[6].strip()) if row[6].strip() != '' else 0
                    if codelength != depth:
                        continue
                    for rootkey, root in roots.items():
                        if root['account_number'] == int(row[2][0:codelength-2]):
                            for slkey, slroot in root.items():
                                if slkey in ['is_group', 'is_root', 'account_type', 'root_type', 'account_number']:
                                    continue
                                if slroot['account_number'] == int(row[2][0:codelength-1]):
                                    
                                    if row[5].strip() == '':
                                        roots[rootkey][slkey].update({account: {'account_number': code, 'is_group' : is_group}})
                                    else:
                                        roots[rootkey][slkey].update({account: {'account_type': row[5].strip(),'account_number': code, 'is_group' : is_group}})

        if depth == 4:
            with open('data.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                next(csv_reader)
                for row in csv_reader:
                    classcode = int(row[0])
                    codelength = int(row[1])
                    code = int(row[2])
                    account = row[3].strip()
                    is_group = int(row[6].strip()) if row[6].strip() != '' else 0
                    if codelength != depth:
                        continue
                    for rootkey, root in roots.items():
                        if root['account_number'] == int(row[2][0:codelength-3]):
                            for slkey, slroot in root.items():
                                if slkey in ['is_group', 'is_root', 'account_type', 'root_type', 'account_number']:
                                    continue
                                if slroot['account_number'] == int(row[2][0:codelength-2]):
                                    for tlkey, tlroot in slroot.items():
                                        if tlkey in ['is_group', 'is_root', 'account_type', 'root_type', 'account_number']:
                                            continue
                                        if tlroot['account_number'] == int(row[2][0:codelength-1]):
                                            
                                            if row[5].strip() == '':
                                                roots[rootkey][slkey][tlkey].update({account: {'account_number': code, 'is_group' : is_group}})
                                            else:
                                                roots[rootkey][slkey][tlkey].update({account: {'account_type': row[5].strip(),'account_number': code, 'is_group' : is_group}})

        if depth == 5:
            with open('data.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                next(csv_reader)
                for row in csv_reader:
                    classcode = int(row[0])
                    codelength = int(row[1])
                    code = int(row[2])
                    account = row[3].strip()
                    is_group = int(row[6].strip()) if row[6].strip() != '' else 0
                    if codelength != depth:
                        continue
                    for rootkey, root in roots.items():
                        if root['account_number'] == int(row[2][0:codelength-4]):
                            for slkey, slroot in root.items():
                                if slkey in ['is_group', 'is_root', 'account_type', 'root_type', 'account_number']:
                                    continue
                                if slroot['account_number'] == int(row[2][0:codelength-3]):
                                    for tlkey, tlroot in slroot.items():
                                        if tlkey in ['is_group', 'is_root', 'account_type', 'root_type', 'account_number']:
                                            continue
                                        for fthkey, fthroot in tlroot.items():
                                            if fthkey in ['is_group', 'is_root', 'account_type', 'root_type', 'account_number']:
                                                continue
                                            if fthroot['account_number'] == int(row[2][0:codelength-1]):
                                                
                                                if row[5].strip() == '':
                                                    roots[rootkey][slkey][tlkey][fthkey].update({account: {'account_number': code, 'is_group' : is_group}})
                                                else:
                                                    roots[rootkey][slkey][tlkey][fthkey].update({account: {'account_type': row[5].strip(),'account_number': code, 'is_group' : is_group}})
                                        


                

data = []       
roots = dict()


for i in range(1, 8):
    walk_roots(i)
    walk_nodes()
    
mydict = {
    "country_code": "ma",
    "name": "Maroc - Plan Comptable General avec code",
    "tree": roots
}

with open("sample.json", "w", encoding="utf-8") as outfile:
    json.dump(mydict, outfile)
    pass