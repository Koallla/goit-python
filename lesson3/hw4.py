import os
import sys

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
path = sys.argv[1]

# files - это список имен файлов и папок в path.
files = os.listdir(path)

photo = []
video = []
docs = []
music = []
soft = []
zip_data = []
other = []
all_files_extension = []

for file in files:
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

# Список всех расширений
    if '.' in file_lower:
        all_files_extension.append(file_lower.split('.')[-1])

# Только уникальные расширения
unique_extension = set(all_files_extension)

print('photo', len(photo), photo)
print('video', len(video), video)
print('docs', len(docs), docs)
print('music', len(music), music)
print('soft', len(soft), soft)
print('zip_data', len(zip_data), zip_data)
print('other', len(other), other)
print('extension: ', len(unique_extension), unique_extension )