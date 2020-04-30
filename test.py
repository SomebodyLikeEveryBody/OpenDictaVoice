import threading

def f():
    ret = 0
    for i in range(0, 15000000):
        ret += 1
    print(ret)

def test():
    x = threading.Thread(target=f)
    print('prets ?')
    print('go !')
    x.start()
    print('ca tourne')
    print('ca tourne toujours')
    print('ca tourne encore')
    print('toussa toussa')
    x.join()
    print('etc etc')
    print('et tralali et tralala')

test()
