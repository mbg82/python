N,B=input().split()
B=int(B)
N=N.upper()
# print(N,B)
res=0

for i in range(len(N)):
    ch=N[i]
    if 0<=ch<=9:
        num=ord(ch)-ord('0')
    else:
        num=ord(ch)-ord('A')+10

    res=res*B+num

print(res)

##################
n, b = input().split()
print(int(n, int(b)))

#############################
A = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','D','F','G','H','I','J','K','L','M','N',
'O','P','Q','R','S','T','U','V','W','X','Y','Z']

N , B = input().split()
b = int(B)
n = len(N)
s = 0
for i in N:
    I = A.index(i)
    s += I*(b**(n-1))
    n -= 1
print(s)


########################################
N, B = input().split()
B = int(B)

num_dict = {str(i): i for i in range(10)}
num_dict.update({chr(i + 55): i for i in range(10, 36)})

total = 0
square = len(N) - 1

index = 0
while index < len(N):
    total += num_dict[N[index]] * (B ** square)
    index += 1
    square -= 1