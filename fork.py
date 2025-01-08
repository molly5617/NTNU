import os, sys

ret = os.fork()
if ret == 0:
    print("子行程:pid={},父行程:pid={}".format(os.getpid(), os.getppid()))
    os.execve("/bin/echo", ["echo", "pid={} 大家好".format(os.getpid())], {})
    exit()
elif ret > 0:
    print("父行程:pid={},子行程:pid={}".format(os.getpid(), ret))
    exit()
sys.exit(1)
