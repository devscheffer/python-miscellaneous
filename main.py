
from src.cls_process_multiple_class import cls_process_multiple_class

path_file = "python-miscellaneous/data/2021_2.yml"
list_subfolder = [
    "1.Task", "2.Reference", "3.Software", "4.Git"
]

cls_process_multiple_class(
    path_file=path_file, list_subfolder=list_subfolder
).mtd_start()
