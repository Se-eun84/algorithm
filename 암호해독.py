#1001010 J
#1000101 E
#1001010 J
#1010101 U

#strip 오른쪽, 왼쪽 공백 제거
#replace() 중간 내용 교체
#ord() : 문자 -> 숫자
#chr() : 숫자 -> 문자

text = ['+ -- + - + -',
        '+ --- + - +',
        '+ -- + - + -',
        '+ - + - + - +']
l=[]
for i in text:
    print(chr(int(i.strip().replace(' ','').replace('+',"1").replace('-','0'),2)))
    l.append(chr(int(i.strip().replace(' ','').replace('+',"1").replace('-','0'),2)))

''.join(l)