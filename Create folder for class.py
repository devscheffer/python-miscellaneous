'''
Cria folders com numero e data para as aulas.
'''

from datetime import datetime, timedelta
from os import path, makedirs

date_start = "2020-08-15"
date_end = "2020-12-22"

date_start = datetime.strptime(f"{date_start}", "%Y-%m-%d").date()
date_end = datetime.strptime(f"{date_end}", "%Y-%m-%d").date()

date = date_start
count = 1
list_folder = []

while date <= date_end:
    folder_name = f"{count:02} - {date}"
    date += timedelta(weeks=1)
    count += 1
    list_folder.append(folder_name)

for i in list_folder:
    if not path.exists(i):
        makedirs(i)
