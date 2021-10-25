n = int(input())
res = 0
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    #tmp=input().split()
    tmp = arr[i]
    # 정렬을 한다.
    tmp.sort()
    a,b,c = map(int, tmp)
    if a == b and b == c:
        money = 10000+a*1000
    elif a == b or a == c:
        money = 1000+a*100
    elif b == c:
        money = 1000+b*100
    else:
        #정렬을 했기 때문에 c가 가장 큰값
        money = c*100
    if money>res:
        res = money
print(res)