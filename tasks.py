from celery import Celery
from time import sleep

app = Celery('tasks', broker='redis://localhost:6379')

@app.task
def  process(x, y):
    i = 0
    while i < 5:
        sleep(1)
        i += 1
        print("Processing...")
        
    return x**2 + y**2 

# if __name__ == '__main__':
    # print(process(2, 3))
    # print(process.delay(2,3))
    
###-----------important-------------
# if you dont have windows subsystem for linux
# then ruun on bash celery -A tasks worker -l info --pool=solo
# but if you do the just run on bash celery -A tasks worker -l info --pool=solo
# then run test on python terminal but make sure you direct to the file first