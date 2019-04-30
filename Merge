import os

with open('MERGED.txt', 'r') as myfile:
      data = myfile.read()
filehandle = open('response.txt', 'w')
filehandle.write(data)


try:
    os.remove('response.txt')
except OSError:
    pass




def looping(req_length):
    for i in range(req_length):
        x = 100001+i
        res = "TR0001000"+str(x)+"00001000000000000000000 000000000000000000000000000000000000000000000000000000000000M  MMM002"
        #new_data = data.replace('1000001',str(x))
        filehandle.write(res)
        filehandle.write("\n")
    filehandle.close()
    
    return str(x)





looping(100)












