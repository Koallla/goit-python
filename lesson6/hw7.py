import os
import sys
from pathlib import Path
from translator import normalize

# Чтобы запутить скрипт, нужно указать путь к папке через переменную path_dir:
path_dir = 'D:\\Auto'
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

# Перевод имени файлов и их переименование (для цикла path.iterdir())
def rename_files (file):
    ext = file.suffix
    print(file.name)

    file_name_without_ext = file.name.removesuffix(ext)
    print('file_name_without_ext:', file_name_without_ext)

    file_name_translated = normalize(file_name_without_ext)
    file_name_with_ext = '{}{}'.format(file_name_translated, ext)
    p = Path(file)
    parent_dir = p.parent
    full_path_new_file = '{}\{}'.format(parent_dir, file_name_with_ext)
    p.rename(full_path_new_file)


   
# Получение всех файлов, в том числе вложенных, 
all_files = list()  

def get_files_list(path):
    for file in path.iterdir():

        if file.is_file():
            rename_files(file)
        
            all_files.append(file.name)
            # Получение уникальных расширений
            extensions(file, unique_extensions)

            ext_lower = file.suffix[1:].lower()
            file_name = file.name

            # if ext_lower in (photo_filter):
            #     photo.append(file_name)

            # elif ext_lower in (video_filter):
            #     video.append(file_name)

            # elif ext_lower in (docs_filter):
            #     docs.append(file_name)

            # elif ext_lower in (music_filter):
            #     music.append(file_name)

            # elif ext_lower in (soft_filter):
            #     soft.append(file_name)

            # elif ext_lower in (zip_data_filter):
            #     zip_data.append(file_name)

        #     else:
        #         extensions(file, unknown_extensions)

        # else:
        #     path = Path(f'{file.parent}\{file.name}')
        #     # Рекурсия
        #     get_files_list(path)
    
get_files_list(path)



# def create_table_string_format(extention, files_list):
#     ''' This funcrion create table for files_list '''

#         width = 20
#         width_file_list = 60

#         string_files = ''
#         for file in files_list:
#             string_files += '| {:^{width}} | {:^{width}} | {:^{width_file_list}} | \n'.format(' ', ' ', file, width=width, width_file_list=width_file_list)


#         title = '| {:^{width}} | {:^{width}} | {:^{width_file_list}} |'.format('Files names', 'Counts', 'Files list',  width=width, width_file_list=width_file_list)
#         line = '=' * len(title)
#         header = line + '\n' + title + '\n' + line + '\n'

#         files_name_and_count = '| {:^{width}} | {:^{width}} | {:_^{width_file_list}} | \n'.format(extention, len(files_list), '', width=width, width_file_list=width_file_list)

#         end = '{:=^{width}}'.format('END', width=len(title))

#         print(header + files_name_and_count + string_files + end)



# create_table_string_format('photo', photo)
# create_table_string_format('video', video)
# create_table_string_format('docs', docs)
# create_table_string_format('music', music)
# create_table_string_format('soft', soft)
# create_table_string_format('zip_data', zip_data)
# create_table_string_format('unknown_extensions', unknown_extensions)
# create_table_string_format('all_extension:', unique_extensions)


