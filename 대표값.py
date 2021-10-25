# 대표 값 출력

n = int(input())
arr = list(map(int, input().split()))

# round = 소수 첫째 자리에서 반올림 한다.
# sum = list의 모든 값을 합한다.
avg = round(sum(arr)/n)

# idx = 학생의 인덱스
# x = 값
# enumerate(): idx에는 인덱스 x는 값을 반환한다.
min = len(arr)+55

for idx, x in enumerate(arr):
    # abs: 값 과의 거리
    tmp = abs(x-avg)

    #거리 값이 가장 가까운 학생이 평균과 가장 가깝다.
    if tmp<min:
        #index와 값 저장
        min = tmp
        score = x
        #학생 번호 저장
        res = idx+1
    #같은 거리가 나왔을 때
    #ex 입력 74
    #배열 73 75 75 75
    # 73하고 거리도 1 75하고 거리도 1
    #답이 2개인 경우
    #큰점수로 출력
    elif tmp== min:
        #작은 번호만 출력이기 때문에 >=가 아님
        if x>score:
            score = x
            res=idx+1

print(avg, res)
