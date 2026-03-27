n,m=map(int,input().split())

def prn():
    for i in range(n):
        print('Hello')

def prn2():
    for j in range(m):
        print('Hello')

prn()
print()
prn2()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def hello_k(count):
    if count > 0:
        print("Hello")
        hello_k(count - 1)

N, M = map(int, input().split())

hello_k(N)
print()
hello_k(M)