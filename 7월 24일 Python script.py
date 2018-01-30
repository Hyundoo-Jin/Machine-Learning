# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:31:17 2017

@author: student
"""

aa = 124
aa = -154

cc = 0o166

a = 10
b = 10

a + b
a ** b
5%2
2%5

3/2
3//2

### // = 몫을 나타내는 연산자
### % = 나머지를 나타내는 연산자

word = 'HELLO WORLD'
"I'm OK"


### 따옴표 세개를 연속으로 입력하면 여러 줄에 걸친 문자열 입력
"""안녕하세요
반갑습니다
"""
d = '''Nice to meet you'''
type(d)
c = 'hello'
c * 3
c + 30
str = "You've got a friend"
str[0:5]
str[0:-1]

str = "20150613121320"
date = str[:8]
time = str[8:]
year = date[:4]
month =date[4:6]
day = date[6:8]
print (date)
print (time)

print (year+"년"+month+"월"+day+"일")

## 문자열, 튜플 자료형은 그요소값을 변경할 수 없다.
aa = 'ABCD'
a = (1, 2, 3, 4, 5)
b = [1, 2, 3, 4, 5]
aa[:1]
aa = aa[:1] + 'F' + aa[2:]
aa


char = 'a b c d e'
char[0:4]


### 문자열 포맷
'제 나이는 %d살 입니다.'%20
'제 나이는 %s살 입니다.'%20
    # %d 숫자, %s 문자열 %f 정수형

'%0.5f' %2.45454545
'%10s' %'hello'
'%-10s' %'hello'
'%-6sPython!!' %'hello'    # 문자열의 위치를 지정할 수 있다.
'%6sPython!!' %'hello'


# 리스트의 형태는 자유롭게 지정할 수 있다.
aa = [10, 20, 30]
movies = ['트랜스포머', '국제시장', '명량']
bb = [10, 20, '명량', '국제시장']
cc = [10, 20, ['명량', '국제시장']]
dd = []
cc[2][1]
[[[[1, 2, 3, 4]]]]

x = [10, 20, 30]
y = [100, 200, 300]
x + y
a = [1, 2, 3, 4]
a[1] = '국제시장'
a[2:] = ['국제시장','명량']
    # append -> 마지막 인덱스 뒤에 추가(추가)
    # extend -> 마지막 인덱스 뒤에 연장(확장)
print(a.append([1, 3, 4]))
a.append([1, 3, 4])
a
a.extend([1, 3, 4])
a



del [a] ### 객체 삭제(Python 내장 함수)




a = {'first' : ['a', 'b', 'c']}
sports = {'축구' : '박지성', '야구' : '박찬호', '체조' : '손연재'}
sports['축구']
aa = {1 : '안녕'}
aa[2] = '하이'
aa[3] = '방가'
aa['age'] = 34
aa

del aa[1]
aa[1] = '안녕'


### Dictionary 주의사항
    # key값은 고유한 값이므로 중복되는 값을 설정하면 안된다.
    # key값에 리스트는 쓸 수 없으나 튜플은 사용할 수 있다.(변화가 불가능하기 때문에)

dict() # 빈 딕셔너리를 만드는 함
bb = {'names' : '홍길동', 'hp' : '010-1234-1234', 'age' : 24}
bb.values()
bb.keys()
keylist = list(bb.keys())
keylist
bb.items()
bb.get('age') ### get은 gender값이 없으면 none이라는 값을 반환한다.
k = bb.get('gender', '없을때출력')
k

### 딕셔너리 안에 특정 값이 있는지 알아보기
'gender' in bb
'age' in bb
bb.pop('names') ### 해당하는 키 값에 해당하는 value를 가져오고 원래의
                # 딕셔너리에서는 해당 키를 삭제한다.
bb.get('names')
bb['names']
len(bb)   ### 객체의 길이를 출력하는 함수





######################### 파일 입출력 #################################
fp = open('test_new.txt', 'w')
for i in range(1, 5) :
    content = '%d번째 줄... \n' %i
    fp.write(content)
fp.close()



fp = open('test_new.txt', 'w')
for i in range(1, 11) :
    content = '%d번째 줄... \n' %i
    fp.write(content)
fp.close()

fp = open('test_new.txt', 'r')
data = fp.readline()
fp.close()

fp = open('test_new.txt', 'r')
while True :
    data = fp.readline()
    if not data : break
    print(data)



# readlines 는 리스트로 값 반환
# read는 하나의 문자열로 값 반환

with open('test_new.txt', 'w') as fp:
    fp.write('with문을 이용한 파일 입출력 테스트')


import pandas as pd
pd.DataFrame()

jumsu = [90, 50, 60, 45, 80]
number = 0
for i in jumsu :
    number = number + 1  ## 혹은 num += 1 로 표현 가능
    if i >= 60 :
        print('%d번 학생의 점수는 %d점으로 합격 되었습니다!'%(number, i))
    else :
        print('%d번 학생의 점수는 %d점으로 불합격 되었습니다!'%(number, i))


for i in jumsu :
    number += 1
    if i < 60 : continue
    print('%d번째 학생 합격입니다!'%number)


aa = [('a', 'b'), ('c', 'd'), ('e', 'f')]    
for (i, j) in aa :
    print (i + j)

for i in range(2, 10) :
    for j in range(1, 10) :
        print(i*j, end = ' ')
    print('')

range(1, 5, 2)

for i in range(1, 9) :   ## else는 if가 없더라도 사용 가능
                            # for문이 한 번 돌 때 마다 else문 시행
    print(i)
else :
    print('반복문 종료')


for i in range(1, 10) :
    for j in range(1, 10) :
        print('%d*%d=%d' %(i, j, i*j), end = ' ')
    print('%d단\n' %i)
gugudan_2 = []
for i in range(1, 10) :
    gugudan_2.append(i*2)
print(gugudan_2)    



### 리스트 내포(List comprehension)의 기본적인 구조
#[표현식 for 항목 in 반복가능한 객체 if 조건]
#[표현식 for 항목1 in 반복가능한 객체1 if 조건1
#           for 항목2 in 반복가능한 객체2 if 조건2]



aa = input('숫자를 입력하세요 >>>')    ### 사용자 프롬프트 만들기
aa
for i in range(5) :
    print(i, end = ' ')
    print('길이는', i)

for i in range(1, 100) :
    if i % 6 == 0 :
        print('%d는 6의 배수' %i)
    elif i % 7 == 0 :
        print('%d는 7의 배수' %i)
    elif i % 9 == 0 :
        print('%d는 9의 배수' %i)
    else :
        print('%d는 정수' %i)

days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
response = input('오늘은 무슨 요일입니까?')
for i in days :
    if response == i :
        print('오늘은 %s 입니다.'%i)
        break
    else :
        print('오류입니다. 처음부터 다시 진행해 주세요')
        break

aa = 0
while aa < 10 :
    aa += 1
    print('aa값은 %d입니다.' %aa)
    if aa == 10 :
        print('종료합니다.')
        
m = 100
n = 10
while m :
    n -= 1
    print('현재 값은 %d입니다.' %n)
    if not n :
        print('n의 값은 0입니다.')
        break

### 홀수만 출력하도록 프로그래밍
i = 0
while i < 10 :
    i += 1
    if i % 2 == 0 : continue
    print(i)
    



print("you've {0} a friend".format('got'))
print("{2} {0} {1}".format("a", 100, 200))

def show_max(a, b) :
    if a > b :
        print('최대값은 %s입니다.'%a)
    elif a== b :
        print('두 값이 같습니다.')
    else :
        print('최대값은 %s입니다.'%b)
show_max(5, 5)
show_max(5, 2)    
show_max(1, 25)    




number = 100
day = '일요일'
print('오늘은 우리가 사귄지 {1}일째 되는 날! 요일은 {0}!!!'.format(day, number))    
m = 1
import numpy as np
num = []
lotto()
def lotto() :
    while m :
        n = int(np.random.uniform(1, 45))
        k = n in num
        if  k == False :
            num.append(n)
            if len(num) == 6 :
                print(num)
                break
##### 나만의 라이브러리 만들기###
def plus(a, b) :
    return a+b
def minus(a, b) :
    return a-b
def multi(a, b) :
    return a*b
def divide(a, b) :
    return a/b    ## 저장해서 워킹 디렉토리 혹은 Lib 폴더에 넣기




import mylib as my  # 라이브러리 전체 import
from mylib import minus   # 라이브러리에서 특정 함수만 import
my.multi(2, 3)

