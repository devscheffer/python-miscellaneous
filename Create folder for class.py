'''
Cria folders com numero e data para as aulas.
finalizado
'''

from datetime import datetime, timedelta
from os import path, makedirs



makedirs("0.CLASS")
makedirs("1.TASK")
makedirs("2.REFERENCE")
makedirs("3.SOFTWARE")

date_start = "2021-03-08"
date_end = "2021-07-12"

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
        makedirs("0.CLASS/"+i)
