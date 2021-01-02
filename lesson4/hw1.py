import os
import sys
from pathlib import Path

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
# path = sys.argv[1]
# print(path)

# files - это список имен файлов и папок в path.
# files = os.listdir(path)

path_dir = 'D:\\Install'
path = Path(path_dir)

files = list()

# print(path.parent)


def get_files_list(path):

    for file in path.iterdir():

        if file.is_file():

            files.append(file.name)

        else:

            path = Path(f'{file.parent}\{file.name}')
            get_files_list(path)


get_files_list(path)

print(len(files))




# print(files)
# photo = []
# video = []
# docs = []
# music = []
# soft = []
# zip_data = []
# other = []
# directs = []
# unique_extension = set()

# # Выделение уникальных расширений
# def extension(file, container):
#     if '.' in file:
#         container.add(file.split('.')[-1])


# def sort_files(some_files):

#     for file in some_files:

#         file_lower = file.lower()

#         if file_lower.endswith('jpg') | file_lower.endswith('jpeg') | file_lower.endswith('png'):
#             photo.append(file)
#         elif file_lower.endswith('avi') | file_lower.endswith('mp4') | file_lower.endswith('mov'):
#             video.append(file)
#         elif file_lower.endswith('doc') | file_lower.endswith('docx') | file_lower.endswith('txt') | file_lower.endswith('pdf') | file_lower.endswith('xlsx'):
#             docs.append(file)
#         elif file_lower.endswith('mp3') | file_lower.endswith('ogg') | file_lower.endswith('wav') | file_lower.endswith('amr'):
#             music.append(file)
#         elif file_lower.endswith('exe'):
#             soft.append(file)
#         elif file_lower.endswith('zip') | file_lower.endswith('rar'):
#             zip_data.append(file)

#             # =====================================================
#         elif '.' not in file_lower:
#             directs.append(file)
#             # print(path(directs))
            
#         else:
#             other.append(file)


#         # Только уникальные расширения
#         extension(file_lower, unique_extension)

    

#     print('photo', len(photo), photo)
#     print('video', len(video), video)
#     print('docs', len(docs), docs)
#     print('music', len(music), music)
#     print('soft', len(soft), soft)
#     print('zip_data', len(zip_data), zip_data)
#     print('other', len(other), other)
#     print('directs', len(directs), directs)
#     print('unique_extension:', len(unique_extension), unique_extension)



# sort_files(files)

