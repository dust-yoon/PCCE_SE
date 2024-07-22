# 함수
    # 1. 선언
def get_bigger(x, y):
    if x > y:
        return x
    else:
        return y
    # 2. 호출
result=get_bigger(3, 6)
print(result)
print(get_bigger(7, 9))

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

# 매개변수 O, 반환값 X
    # 데이터를 입력 받아 처리하지만 값을 반환할 필요 없는 경우
    # return 이 없으면 함수의 결과를 별도 변수로 할당할 수 없다. 
def say_hello(name):
    print(f'안녕하세요, {name}님!') # 안녕하세요, 김건국님!
result = say_hello('김건국')
print(result) # None
# 안녕하세요, 김건국님!
# None <class 'NoneType'>

# 매개변수 X, 반환값 O
    # 입력 없이 항상 정해진 처리만 하고 값을 반환하는 경우
def even_numbers():
    a = []
    for i in range(1, 11):
        if i % 2 == 0:
            a.append(i)
    return a
numbers = even_numbers()
print(numbers)

# 매개변수 X, 반환값 X
    # 입력 없이 항상 정해진 처리만 하면서 값도 반환할 필요가 없는 경우
def welcome():
    print("Welcome to Python world!")
welcome()


## 구현연습
def solution(money):
    answer = []
    price = 5500
    answer.append(money//price)
    answer.append(money%price)
    return answer
print(solution(15000))



## 내장함수
# print(a) : a 를 출력
# len(a) : a 의 길이를 변환

numbers = [24, 23, 22, 21, 20, 19, 18, 17]
print(sum(numbers))
# sum 기능 구현
def sum_func(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

a = [3, 1, 0, 5, 31]

print(sorted(a))
print(sorted(a, reverse=True))
print(a)

numbers = [17, 20, 24, 18, 21, 19, 23, 22]
print(sorted(numbers, reverse=True))
print(list(reversed(numbers)))
print(numbers[::-1])
print(numbers) # 웑본자료 수정하지 않음


## 리스트
# 특징 : 순서가 있는 컨테이너, 기변 자료형
a = [1,0, 2, 3, 'four', '6']
a[0] =1
print(a.append(7)) # 맨 끝에 추가
print(a)
a.insert(1,8) # 중간에 추가
last_value = a.pop(1) # 1번에 위치한 삭제값 반환
print(last_value)
# pop -> 반환값이 있다.
remove_value = a.remove(1) # 1이라는 값이 처음 발생한 부분의 값을 삭제함 반환값은 없음

a = [1, 44, 2, 4, 6, 23]
a.sort()
print(a)
a.reverse()
print(a)
a.append([1, 2, 4])
a.extend([1, 2, 4])
print(a)

print(a.count(2))


## 문자열 메소드
students = ['alex', 'kyle', 'jun', 'justin']
print('님, '.join(students))