import random
from os import path

def random_id(length,FileType):
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTUVWXYZ'
    id = ''
    for i in range(0,length,2):
        id += random.choice(number)
        id += random.choice(alpha)
        var_id = id+str('.')+FileType
    return var_id


try:
    a = 20
    print(a/0)
except(ZeroDivisionError) as er:
    print('Error message',er)



