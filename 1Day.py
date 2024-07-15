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

# 추가 학습 자료
users = {
    'total_user' : 3,
    'information' : [
        {'name' : 'Alex', 'age' : 3, 'license': True},
        {'name' : 'June', 'age' : 7, 'license': False},
        {'name' : 'Peter', 'age' : 4, 'license': False}
    ]
}


## 변수
# 알파벳, 언더바(_), 숫자로만 구성되어야 함
# 첫 글자에는 숫자가 올 수 없음
# 대소문자를 구별할 줄 알아야 함
# 띄어쓰기가 필요할 경우 언더바로 표시
# 예약어는 사용하지 않음

name = '김건국'
print('안녕하세요, ', name)

# break = 'a'
# # syntex highlighting : 예약어 의심 예약어 유의사항
# print(break) - 더이상 함수로서의 역할을 할 수 없게 됨.
# 식별자 = Literal




## 자료형(Data types)
# 숫자형(Numeric type)-정수(Integer),실수(Float)//문자열(String type)//불린형(Boolean type)-참(True),거짓(False)

# 숫자형

# 1. 정수 (integer -> int)
print(type(0)) # 자료형 확인 내장 함수 <class 'int'> 출력
print(1)
print(-2)

# 2. 실수 (float) 소수점이 포함되어 있음
print(type(1.2))
print(type(-3.14))

# 어떤 자료형이 나오게 될까? -> <class 'float'> 인데 <class 'int'>로 변환
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


# 불린형
# 공백은 False형 자료라고 볼 수 있음 (list 도 비어있으면 거짓 불린의 형태로 취급)
# 조건문에서 유용하게 활용
# 명시적 형변환은 Notion 참고(int(4.01)=4)

num = 0
print(num)
print(type(num))
print(bool(num))
# False

s = '123'
print(s)
print(type(s))
print(bool(s))
# True

s = '0'
print(s)
print(type(s))
print(bool(s))
# True

lst = [1]
print(lst)
print(type(lst))
print(bool(lst))
# True(리스트 안에 내용이 존재함)