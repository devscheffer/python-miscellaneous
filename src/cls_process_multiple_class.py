import yaml

from src.cls_folder_structure import cls_folder_structure


class cls_process_multiple_class:
    def __init__(self, path_file, list_subfolder):
        self.path_file = path_file
        self.list_subfolder = list_subfolder

    @property
    def path_file(self):
        return self.__path_file

    @path_file.setter
    def path_file(self, path_file):
        self.__path_file = path_file

    @property
    def list_subfolder(self):
        return self.__list_subfolder

    @list_subfolder.setter
    def list_subfolder(self, list_subfolder):
        self.__list_subfolder = list_subfolder

    def mtd_start(self):
        data = self.mtd_file_read()
        count = 0
        for key in data:
            class_name = key
            date_start = data[key]["date"][0]
            date_end = data[key]["date"][1]
            order = count
            cls_folder_structure(
                class_name=class_name
                , date_start=date_start
                , date_end=date_end
                , order=order
                , list_subfolder=self.list_subfolder
            ).mtd_start()
            count += 1

    def mtd_file_read(self):
        with open(self.path_file, "r", encoding="utf-8") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            data_sort = dict(
                sorted(
                    data.items(),
                    key=lambda x: x[1]["date"][0], reverse=False
                ))
        return data_sort
