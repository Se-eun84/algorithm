n = int(input("입력 : "))

ch = [0]*(n+1)

cnt = 0

for i in range(2,n+1):
    if ch[i]==0:
        print("소수 : ", i)
        cnt+=1
        # 마지막 i씩 증가한다.
        for j in range(i, n+1, i):
            ch[j] = 1
print("소수의 개수 : ", cnt)
