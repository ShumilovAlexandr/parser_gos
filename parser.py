import os

from ftp_obj import FTPConnectionView


class DirList:

    def __init__(self):
        self.ftp = None
        self.dir_list = []

    def connect_ftp(self):
        self.ftp = FTPConnectionView()
        self.ftp.connect()
        self.ftp.login()

        # Нужно перейти в директорию с папками по регионам и установить ее
        # как рабочую
        self.ftp.cwd('fcs_regions')

    def get_list_directories(self):
        """Метод нужен для получения списка директорий в текущем каталоге."""
        self.connect_ftp()

        # Нужно будет исключить лишние директории при получении названий
        # регионов
        exclude = ['temp_err', 'eacts', 'ERUZ', 'fcs_undefined', 'PG-PZ', 'control99docs']

        try:
            for dirname in self.ftp.nlst():
                if not dirname.startswith('_') \
                        and '.' not in dirname\
                        and not any(x in dirname for x in exclude):
                    self.dir_list.append(dirname)
        except Exception as e:
            print(e)    # TODO заменить логированием. Точнее, добавить
        return self.dir_list

    def get_list_files(self):
        """
        Тут нужно получать список файлов в текущей директории с которыми
        будем работать.
        """
        pass




f = DirList()
print(f.get_list_directories())

