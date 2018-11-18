import sys
import os
import pandas as pd
from collections import defaultdict
import re

# get ID
id_c = re.compile(r'\d+')
data_folder = './data/'
def getId(line):
    return id_c.match(line).group(0)

src_file = '16-10-us.txt'
alter_file = '16-clean.txt'
with open(src_file, 'r', errors='replace', encoding='utf-8') as f:
    with open(alter_file ,'w') as w:
        w.write(f.read())

print('finish write new utf-8')

# devide a whole file to different files to decrease the file size
record = defaultdict(list)

with open(alter_file) as k:
    for line in k.readlines():
        record[getId(line)].append(line)

print('finish new lines')

for k, v in record.items():
    with open(os.path.join(data_folder, k + '.txt'), 'w') as w:
        w.write(''.join(v))