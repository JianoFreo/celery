from celery import Celery
from time import sleep

app = Celery('tasks', broker='redis://localhost:6379', backend="redis://localhost:6379")

@app.task
def  process(x, y):
    i = 0
    while i < 5:
        sleep(1)
        i += 1
        print("Processing...")
        
    return x**2 + y**2 

# process.delay(2, 3)
# result = process.delay(2, 3)
# result.get() ##Grabs the value from redis

# result = process.AsyncResult('2cdb669c-93f7-4602-9a33-3abcd1e2c3ae') ##The ID of the result
# To test the results:
    # result.status() or result.status  #if ran on the terminal   =====Equal to 'SUCCESS'=======
    # result.result() or result.result or result.get() ===equal to === the return value
    
# if __name__ == '__main__':
    # process(2, 3)
    # process.delay(2,3)
    
###-----------important-------------
# if you dont have windows subsystem for linux
# then ruun on bash celery -A tasks worker -l info --pool=solo
# but if you do the just run on bash celery -A tasks worker -l info --pool=solo
# then run test on python terminal but make sure you direct to the file first