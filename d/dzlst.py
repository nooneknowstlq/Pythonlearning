f = open('text2.txt', 'w')
f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать строку в файл;")
f.close()

f = open('text2.txt', 'r')
read_file = f.readlines()
print(read_file)
read_file[1] = "Hello world!\n"
print(read_file)
f.close()

f = open('text2.txt', 'w')
f.writelines(read_file)
f.close()