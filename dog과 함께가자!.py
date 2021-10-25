돌의내구도 = [1, 2, 1, 4]
# 딕셔너리: Key와 Value가 있는 자료형
#  ex) "이름" = "홍길동", "생일" = "몇 월 며칠" 등
독 = [{
    "이름" : "루비독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "4",
    },{
    "이름" : "피치독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "3",
    },{
    "이름" : "씨-독",
    "나이" : "72년생",
    "점프력" : "2",
    "몸무게" : "1",
    },{
    "이름" : "코볼독",
    "나이" : "59년생",
    "점프력" : "1",
    "몸무게" : "1",
    },]

import json
JSON독 = json.dumps(독, ensure_ascii=False)
#list로 처리
JSON독 = json.loads(JSON독)

def 징검다리(돌의내구도, JSON독):
    # 독의 이름 출력
    answer=[JSON독[i]['이름'] for i in range(len(JSON독))]
    for i in JSON독:
        독의위치 = 0
        # 돌의 내구도 배열을 벗어나는 것은 돌을 건넌것.
        while 독의위치 < len(돌의내구도)-1:
            # 독의 위치 수정
            독의위치 += int(i['점프력'])
            #돌의 내구도 깍기
            돌의내구도[독의위치-1] -= int(i['몸무게'])
            if 돌의내구도[독의위치-1]<0:
                # 출력값 삭제하기
                del answer[answer.index(i['이름'])]
                break
    return [i for i in answer if i != 'fail']

print(징검다리(돌의내구도.copy(), 독.copy()))