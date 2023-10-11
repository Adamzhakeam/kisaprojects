def f():
    for i in range(10):
        if i==4:
            print('reached 4...')
            return
        print(i)
        
    print('end of function...')

f()