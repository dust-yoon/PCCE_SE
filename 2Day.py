## 산술 연산자
# +,-,/,*(사칙연산)

a = 5 # 정수 int
b = -10 # 정수 int

print(a + b) # -5
print(a - b) # 15
print(int(b / a)) # -2.0 int/int 나누어도 float 값이 도출됨
print(a * b) # -50

# 몫 / 나머지 - 홀짝 구분 짓는 데에 많이 사용됨.
print(b // a) # 몫 2
print(b % a) # 나머지 ...8

# 제곱
print(2**3) # 8


## 복합연산자 - 변수에 다시 재할당하는 시스템이다 보니 대체할 다른 경우가 많이 존재함. 
a += b
a = a + b


## 비교연산자 - 문자열 부분에 다른 문자열이나 수식이 들어가도 상관없음
a = 1
b = 3

print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)


## 논리연산자 - 예시 숙지
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

print(not True)        # False
print(not False)       # True
print(not 0)         # True
print(not "")        # True
print(not "python")  # False
print(1 == 2 and "hi" == "hi")  # False and True == False
print(5 > 2 or 0 != 0)          # True or False == True
print(not 4 <= 3)               # not False == True


## 조건문(bool값 인지) - 들여쓰기 필수(4 space, 1 tab)
bool1 = 2 < 5
print(bool1)

if bool1:
    print('조건이 참입니다.')
else:
    print('조건이 거짓입니다.')

print('이 코드는 무조건 실행이 됩니다. 들여쓰기가 되지 않아서 .')

# number라는 값 짝수인지 홀수인지 확인하기
number = int(input("짝수인가요?: "))
condition = number % 2 == 0
condition2 = number != 0

if condition and condition2:
    print("짝수입니다.")
else:
    if condition:
        print("0입니다.")
    else:
        print("홀수입니다.")




## 컨데이너 자료형(container)
# 순서가 있는 자료형(sequence) - List, String, Range / 순서가 없는 자료형(Non-sequence)

# list (순서가 있는 가변(재할당 가능) 컨테이너 자료형)

data = [10, 1.5, "python", False]

print(data)
print(type(data)) # class <list>
print(len(data)) # 4

list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9,10]

print(list1 + list2) # [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
# print(list1 * list2) # Error : can't multiply sequence by non-int of type 'list'
print(list1 * 2)
list3 = [0] * 10
print(list3)
print(list1[-2]) # +-{len(list1)-1} 까지 가능
print(list1[-5])
print(list1[4])

#list_name[start:end:step]
a = [10, 20, 30, 40, 50]
# 예제 숙지
a[1:4:2]   # [20, 40]
a[-5:-2:2] # [10, 30]
a[1:4:-1]  # []
a[4:1:-1]  # [50, 40, 30]
a[2:-1]    # [30, 40]
a[::-1]    # [50, 40, 30, 20, 10] 효율 높은 코드


# string (순서가 있는 불변 컨테이너 자료형)

sentence = "hello python"
print(len(sentence)) #12(공백포함)

word = "python"
new_word = "j" + word[1:]  # 문자열 덧셈과 슬라이싱을 이용하여 마치 수정한 것과 같은 효과를 줄 수 있다.
print(new_word)

s = "abcdefghi"

s[2:-4]    # cde
s[2:5:-1]  # 
s[:]       # abcdefghi
s[::-1]    # ihgfedcba
s[::]      # abcdefghi 

# f-string
university = '건국대학교'
day = 2
sentence1 = f"{university} 학생 여러분, {day}일차 강의를 열심히 들어주셔서 감사합니다."
print(sentence1)

# range (반복문 할 때 한번 더 할거임.)


## 간단한 아보카도 어쩌구 예시 컨테이너 자료형 이용
shopping_list = []
mart = ['avocado', 'banana', 'milk', 'egg']
if "avocado" in mart:
    shopping_list += ['milk'] * 6
else:
    shopping_list.append('milk')

print(shopping_list)

shopping_list = []
mart = ['avocado', 'banana', 'milk', 'egg']
shopping_list.append('milk')

if "avocado" in mart:
    shopping_list += ['avocado']

print(shopping_list)
print(len(shopping_list))