

with open('base.dat', 'r') as myfile:
      data = myfile.read()
#filehandle = open('helloworldtest.dat', 'w')
#filehandle.write(data)

def new_function(value1,value2):
    with open('{}.dat'.format(value1),'w') as f:
            for p in range(value2[0],value2[1] + 1):
                print p
                x = 100000+p
                new_data = data.replace('1000001',str(x))
                f.write(new_data)
            f.close()


def looping(req_length,tuple1):
    l = req_length/10

    a = []
    for i in range(l):
        a.append('file{}'.format(i))

    for j in range(len(a)):
        new_function(a[j],tuple1[j])

results = []
def cal(req_len):
    a = req_len/10
    for i in range(10,req_len +1,10):
        r = i - 9
        result = (r,i)
        results.append(result)
    return results



calculatelist = cal(100)

looping(100,calculatelist)
