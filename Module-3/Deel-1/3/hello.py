def hello(num):
    a = ''
    for i in range(1,num+1):
        a += (f"Hello from function town{i}!\n")
    return a
if __name__ == '__main__':
    for i in range(10):
        print(hello(i))