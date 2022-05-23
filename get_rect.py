import time

tid = time.time()

tid_1 = 0

while True:
    if tid - tid_1 > 1:
        print ('yes')
        tid_1 = tid

    else:
        print (tid)
    

