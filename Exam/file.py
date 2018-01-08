file_object = open('text.txt')
data=file_object.read()
print(data)
#file_object.close()
print('mto hai ba')

file_object.seek(0)# = open('text.txt')
list_content = file_object.readline()
print(list_content)

file_object.seek(0)
list_content = list(file_object)
print(list_content)

file_object.seek(0)
list_content = tuple(file_object)
print(list_content)

file_object.close()