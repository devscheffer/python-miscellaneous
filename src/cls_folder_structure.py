import os
from datetime import datetime, timedelta


class cls_folder_structure:
    """
    Cria folders com numero e data para as aulas.
    finalizado
    """

    def __init__(self, class_name,date_start, date_end,order,list_subfolder) -> None:
        self.class_name = class_name
        self.date_start = date_start
        self.date_end   = date_end
        self.order      = order
        self.list_subfolder = list_subfolder

    @property
    def path_output(self):
        weekday = self.date_start.strftime("%a")
        path = f"./output/{self.order} - {weekday} - {self.class_name}"
        return path

    @property
    def date_start(self):
        return self.__date_start

    @date_start.setter
    def date_start(self, value):
        self.__date_start = self.convert_date(value)

    @property
    def date_end(self):
        return self.__date_end

    @date_end.setter
    def date_end(self, value):
        self.__date_end = self.convert_date(value)

    def mtd_start(self):
        self.mtd_create_main_folder()
        self.mtd_create_subfolder_class()

    def mtd_create_main_folder(self):
        for i in self.list_subfolder:
            path = f"{self.path_output}/{i}"
            os.makedirs(path, exist_ok=True)

    def mtd_create_subfolder_class(self):
        date_start = self.date_start
        date_end = self.date_end
        date = date_start
        count = 1
        subfolder_name = "0.Class"
        while date <= date_end:
            new_folder_name = f"{count:02} - {date}"
            date += timedelta(weeks=1)
            count += 1
            path = f"{self.path_output}/{subfolder_name}/{new_folder_name}"
            os.makedirs(path, exist_ok=True)

    def convert_date(self, date):
        date_input_format = "%d/%m/%Y"
        res = datetime.strptime(date, date_input_format).date()
        return res
