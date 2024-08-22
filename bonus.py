
def read_file (filename):
    file = open(filename, 'r')
    data = file.readlines()
    file.close()
    return data

def file_write(filename,content):
    file = open(filename, "w")
    file.writelines(content)
    file.close()


f_name = "data/doc.txt"
name = input("Enter the name : ").strip() + "\n"
data = read_file(f_name)
data.append(name.title())
file_write(f_name,data)