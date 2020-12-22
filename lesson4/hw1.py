import os
import sys

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
path = sys.argv[1]

# files - это список имен файлов и папок в path.
files = os.listdir(path)

# Только уникальные расширения
def extension(file, container):
    if '.' in file:
        container.add(file.split('.')[-1])
    return container



def sort_files(some_files):
    photo = []
    video = []
    docs = []
    music = []
    soft = []
    zip_data = []
    other = []
    unique_extension = set()

    for file in some_files:

        file_lower = file.lower()

        if file_lower.endswith('jpg') | file_lower.endswith('jpeg') | file_lower.endswith('png'):
            photo.append(file)
        elif file_lower.endswith('avi') | file_lower.endswith('mp4') | file_lower.endswith('mov'):
            video.append(file)
        elif file_lower.endswith('doc') | file_lower.endswith('docx') | file_lower.endswith('txt') | file_lower.endswith('pdf') | file_lower.endswith('xlsx'):
            docs.append(file)
        elif file_lower.endswith('mp3') | file_lower.endswith('ogg') | file_lower.endswith('wav') | file_lower.endswith('amr'):
            music.append(file)
        elif file_lower.endswith('exe'):
                soft.append(file)
        elif file_lower.endswith('zip') | file_lower.endswith('rar'):
            zip_data.append(file)
        else:
            other.append(file)

        # Только уникальные расширения
        extension(file_lower, unique_extension)




    print('photo', len(photo), photo)
    print('video', len(video), video)
    print('docs', len(docs), docs)
    print('music', len(music), music)
    print('soft', len(soft), soft)
    print('zip_data', len(zip_data), zip_data)
    print('other', len(other), other)
    print('unique_extension:', len(unique_extension), unique_extension)



sort_files(files)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))