import numpy as np

def fun(temp):
    temp = round(np.random.rand()*5 + 30)
    humidity = round(np.random.rand()*10 + 60)
    # return {'temperature':temp, 'humidity':humidity}
    return (temp, humidity)

    