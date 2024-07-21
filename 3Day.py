## 반복문 (for횟수O-컨테이너와 함께/while-조건과 함께)


## for 문 (반복=횟수가 정해져 있는 형태)
students = ['김건국', '이국건', '안강남' , '한가양'] #리스트

for student in students:
    print(f'안녕하세요, {student}님. 반갑습니다.')


print(student)
# for 문에서 가장 마지막에 할당된 값이 남아 있음.
# 한가양 ==> 출력

numbers = [1,2,3,4,5]

for number in numbers:
    if number % 2 == 1:
        print(str(number))

for number in list(range(1,6)):
    if number % 2 == 1:
        print(str(number))

print(numbers[0])
print(numbers[2])
print(numbers[4])

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        print(i)

print(len(numbers))



## while 문
# 반복 -> 조건을 만족할 때(조건이 True일 때)까지 반복

i = 0 
numbers = list(range(1,11))
while i < len(numbers):
    if numbers[i] % 2 ==0:
        print(numbers[i])
    i += 1
# 들여쓰기 주의해서 작성해야 하는 이유
i = 0 
numbers = list(range(1,11)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while i < len(numbers):
    if numbers[i] % 2 ==0:  # 첫번째 값이 짝수가 아님
        print(numbers[i])   # 하단의 코드는 실행이 되지 않음
    i += 1              # 증감 또한 되지 않아서, i = 0 (무한하게)
# 이렇게 실행할 경우 코드는 작동하지 않음
# 그럼 만약 처음의 코드가 실행이 된다면? = 처음 코드만 실행되고 마는 코드가 되는 것임. 
numbers = [1, 2, 3, 4, 5]
while numbers:  # 조건 (numbers가 비는 순간 반복 종료)
    deleted_number = numbers.pop()  # numbers의 마지막 원소 삭제 및 반환
    print(deleted_number)

print(numbers)  # []



## contonue 와 break 문
# break
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
    if number == 3:
        print("반복을 종료합니다.")
        break
        print("이 부분은 실행되지 않습니다.") 
# continue
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number % 2 == 0:
        continue 
    print(number)
number = 0

while number <= 5:
    number += 1
    if number % 2 == 0:
        continue
    print(number)




## 기초 자료구조와 로직설계
# 1등급의 광물이 존재하는가
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1] 
# 방법1 : in 연산자 사용하기
if 1 in gems:
    print('1등급의 광물이 존재합니다.')
else:
    print('1등급의 광물이 존재하지 않습니다.')

# 방법2: for 문을 사용하기
grade = False
for gem in gems:
    if gem == 1:
        grade = True
        break # 효율성을 위한 break
if grade:
    print('1등급의 광물이 존재합니다.')
else:
    print('1등급의 광물이 존재하지 않습니다.')

# 1등급의 광물이 몇 개 존재하는가
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
i = 0
number = 0
while i < len(gems):
    if gems[i] == 1:
        number += 1
    i += 1
print(f'1등급의 광물이 {number}개 존재합니다. ')
# 방법1 - 딕셔너리
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grades = {1:0, 2:0, 3:0}
for gem in gems:
    grades[gem] += 1
print(grades)
# 방법2 - 리스트를 통한 구조화
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grades = [0] * 3
for gem in gems:
    grades[gem-1] += 1
print(grades)
# 이용도구 key 값
mapping = {'key1':'key1의 값', 2:0, 3:0} # 딕셔너리를 만들어 냄
# 카 : 값 -> 매핑
print(mapping['key1'])



## max(),min() 구현 실습
nums = [7, 1, 2, 4, 6, 8, 3]
print(min(nums))
print(max(nums))
# 반복문, 조건문을 이용해 max_value, min_value 구현해내기 
    # 논리
    # 1. 반복문을 통해 nums의 숫자를 하나씩 받는다.
    # 2. 초기값과 할당받은 숫자를 비교를 한다.
    # 3. 초기값과 숫자 중, 큰 숫자를 max_value에 집어 넣는다.
    # 4. 반복이 완료되고, max_value를 출력한다.
nums = [7, 1, 2, 4, 6, 8, 3]
i = 0
min_value = nums[0]
while i < len(nums):
    i += 1 
    if nums[i-1] <= min_value:
        min_value = nums[i-1]
print(min_value)

nums = [7, 1, 2, 4, 6, 8, 3]
i = 0
max_value = nums[0]
while i < len(nums):
    i += 1 
    if nums[i-1] >= max_value:
        max_value = nums[i-1]
print(max_value)


for i, num in enumerate(nums):
    print(f'{i+1}번째 반복')
    if num > max_value:
        max_value = num
print(max_value)

for num in nums:
    if num < min_value:
        min_value = num
print(min_value)

i = 0
max_value = 0
while i < len(nums):
    if nums[i] > max_value:
        max_value = nums[i]
print(max_value)