from create_folder_for_class import cls_folder_structure


import yaml

with open(r'python-miscellaneous\2021_2.yml', 'r', encoding='utf-8') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    for i in data:
        class_name = i
        date_start = data[i]['date'][0]
        date_end = data[i]['date'][1]
        order = data[i]['order']
        cls_folder_structure(
            class_name
            , date_start
            , date_end
            , order
            ).mtd_start()
