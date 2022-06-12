
#计算时间
import time

def cal_time_decoration(fuc):
    def wrapper(*args,**kwargs):
        t1=time.time()
        result=fuc(*args,**kwargs) #注意要对应好
        t2=time.time()
        print("%s running time: %s secs."%(fuc.__name__,t2-t1))
        return result
    return wrapper