import os
import sys
from pathlib import Path

# Чтобы запутить скрипт, нужно указать путь к папке через переменную path_dir:
path_dir = 'D:\\Install'
path = Path(path_dir)

photo = []
video = []
docs = []
music = []
soft = []
zip_data = []
unknown_extensions = set()
unique_extensions = set()

# Фильтры для файлов
photo_filter = ("jpeg", "png", "jpg", "svg")
video_filter = ("avi", "mp4", "mov", "mkv")
docs_filter = ("doc", "docx", "txt", "pdf", "xlsx", "pptx")
music_filter = ("mp3", "ogg", "wav", "amr")
soft_filter = ("exe", "mdf", "mds")
zip_data_filter = ("zip", "gz", "rar")

# Выделение уникальных расширений
def extensions (file, container):
    container.add(file.suffix[1:].lower())
   
# Получение всех файлов, в том числе вложенных, 
all_files = list()  

def get_files_list(path):
    for file in path.iterdir():

        if file.is_file():
            all_files.append(file.name)
            # Получение уникальных расширений
            extensions(file, unique_extensions)

            file_lower = file.suffix[1:].lower()
            file_name = file.name

            if file_lower in (photo_filter):
                photo.append(file_name)

            elif file_lower in (video_filter):
                video.append(file_name)

            elif file_lower in (docs_filter):
                docs.append(file_name)

            elif file_lower in (music_filter):
                music.append(file_name)

            elif file_lower in (soft_filter):
                soft.append(file_name)

            elif file_lower in (zip_data_filter):
                zip_data.append(file_name)

            else:
                extensions(file, unknown_extensions)

        else:
            path = Path(f'{file.parent}\{file.name}')
            # Рекурсия
            get_files_list(path)
    
get_files_list(path)


def create_table_string_format(extention, files_list):
    ''' This funcrion create table for files_list '''

        width = 20
        width_file_list = 60

        string_files = ''
        for file in files_list:
            string_files += '| {:^{width}} | {:^{width}} | {:^{width_file_list}} | \n'.format(' ', ' ', file, width=width, width_file_list=width_file_list)

        # Формируем таблицу для файлов
        title = '| {:^{width}} | {:^{width}} | {:^{width_file_list}} |'.format('Files names', 'Counts', 'Files list',  width=width, width_file_list=width_file_list)
        line = '=' * len(title)
        header = line + '\n' + title + '\n' + line + '\n'


        files_name_and_count = '| {:^{width}} | {:^{width}} | {:_^{width_file_list}} | \n'.format(extention, len(files_list), '', width=width, width_file_list=width_file_list)

        end = '{:=^{width}}'.format('END', width=len(title))

        print(header + files_name_and_count + string_files + end)



create_table_string_format('photo', photo)
create_table_string_format('video', video)
create_table_string_format('docs', docs)
create_table_string_format('music', music)
create_table_string_format('soft', soft)
create_table_string_format('zip_data', zip_data)
create_table_string_format('unknown_extensions', unknown_extensions)
create_table_string_format('all_extension:', unique_extensions)
