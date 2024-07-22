## random 모듈
# 랜덤으로 난수를 생성하는 모듈
import random
# 1개의 '정수' 난수를 반환
number = random.randint(1,5)
print(number)
# 1개의 값을 반환
numbers = [24, 22, '23학번', 18, 19, 20, 21]
number = random.choice(numbers)
print(number)
# 원하는 개수만큼 뽑기
student = random.sample(numbers, 3)
print(student)

## time 모듈 - 시간을 다루는 기능
import time
time.sleep(10)
print('10초 후에 출력됩니다.')


## 카운트다운이 있는 로또 추첨기 만들기
import random
import time
i = 0
for i in range(5,0,-1):
    print(f'{i}초 남았습니다.')
    time.sleep(1)
print(sorted(random.sample(range(1,46),6)))
# 동일
numbers = list(range(1, 46))
lotto = random.sample(numbers, 6)
lotto.sort() # lotto 자체를 바꾸고, 별도의 반환되는 값은 없다
# sorted(lotto) # lotto 를 바꾸지 않고, 별도의 새로운 리스트를 반환한다.
print(lotto)


## 구구단을 만들어보자!
for i in range(1, 10):
    print(f'{i}단 입니다.')
    for j in range(1, 10):
        print(f'{i} X {j} = {i*j}')

## 이중 for 문을 이용한 이차원 리스트
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]
for i in range(3):  # 3행
    for j in range(4):  # 4열
        print(matrix[i][j], end=" ")
    print()

num_list = [1, 3, 5, 2, 12]
for i in range(len(num_list)):
    for j in range(num_list[i]):
        print(num_list[i], end = ' ')
    print()

## 모든 원소의 합 구하기
matrix = [
    [0, 5, 3, 1],
    [4, 6, 10, 8],
    [9, -1, 1, 5]
]
matrix[0][1]
print(len(matrix)) # 3 행의 개수만 나옴
print(len(matrix[2]))
# 행과 열 개수 뽑는 코드 만들어보기
count = [0] * 2
for i in range(len(matrix)):
    count[0] += 1
    for j in range(len(matrix[i])):
        count[1] += 1
print(count)
# 이차원 리스트의 순회(모든 값의 합) - for 문 2번 중첩
total = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
            total += matrix[i][j]
print(total)
# (심화) 이차원 리스트의 델타 탐색
def solution(num_list):
    answer = []
    for num in num_list:
        answer.append(0)
        if num == 2:
            answer.pop()
            answer.append(True)
        else:
            for i in range(2,num):
                if num % i == 0:
                    answer.pop()
                    answer.append(False)
                    break # 아예 이 반복을 마침 continue가 아님
                else:
                    answer.pop()
                    answer.append(True)
    return answer

def solution(num_list):
    answer = []
    for num in num_list:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break # 효율성을 위한 반복문 중단
        answer.append(is_prime)
    return answer