import os

with open('Accounts.txt', 'r') as myfile:
      data = myfile.read()
filehandle = open('results.txt', 'w')
filehandle.write(data)


try:
    os.remove('results.txt')
except OSError:
    pass

def looping(req_length):
    for i in range(req_length):
        x = 100001+i
        new_data = data.replace('1000001',str(x))
        filehandle.write(str(x)+"-1")
        filehandle.write("\n")

    filehandle.close()
    return "success"

looping(100)
