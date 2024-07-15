print("alex") # 이름 -> 문자열
print(3) # 나이
print(True) # 운전면허 보유

# 변수 -> 재사용
name = 'alex' # str
age = 3 # int
license = True # bool
gender = 'Male' # str

# 컨테이너 자료형 - 리스트
names = ['alex', 'jun', 'kyle']

student1 = ['alex', 3, True, 'Male'] # 학생 한명의 정보
print(student1[0])

student1[1] =20
print(student1)

# 컨데이너 자료형 - 딕셔너리
student2 = {'name' : 'alex',
            'age' : 20,
            'lisence' : True,
            'gender' : 'Male' }

# 변수

name = '김건국'
print('안녕하세요, ', name)

# break = 'a'
# # syntex highlighting : 예약어 의심 예약어 유의사항
# print(break)


# 숫자형

# 1. 정수 (integer -> int)
print(type(0)) # 자료형 확인 내장 함수 <class 'int'> 출력
print(1)
print(-2)

# 2. 실수 (float)
print(type(1.2))
print(type(-3.14))

# 어떤 자료형이 나오게 될까? -> float
print(type(int(3.0)))

# 문자열 (string -> str)

name = 'alex' # 따옴표(큰 따옴표, 작은 따옴표 상관 없음) 사이에 있는 글자 -> 문자
gender = 'male'

print(name)
print(type(gender))

age = '20'
print(type(age))

nickname = '123python!@#!@#$'
print(type(nickname))

# name = "jun' - 따옴표들 세트로 작성하지 않으면 에러 발생

test = '' # 빈 문자열도 문자열
space = '   ' # 공백(white space)도 문자열

print(type(test))

# 불린형 - 명시적 형변환
num = 0
print(num)
print(type(num))
print(bool(num))

s = '123'
print(s)
print(type(s))
print(bool(s))

s = '0'
print(s)
print(type(s))
print(bool(s))

lst = [1]
print(lst)
print(type(lst))
print(bool(lst))