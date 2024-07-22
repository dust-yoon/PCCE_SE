# bool1 = 2 < 5
# bool2 = True == "True" # bool 값과 연산자 값이라서 같지 않음
# if bool1 :
#     print("출력되게 하세요.")
# if bool2 :
#     print("출력되지 않게 하세요.")

# number = int(input("짝수인가요?: "))
# condition = number % 2 == 0
# condition2 = number != 0
# if condition and condition2:
#     print("짝수입니다.")
# else:
#     if condition:
#         print("0입니다.")
#     else:
#         print("홀수입니다.")

# for i in range(1, 11):
#     print(i, end=" ")

# shopping_list = []
# mart = ['avocado', 'banana', 'milk', 'egg']
# if "avocado" in mart:
#     shopping_list += ['milk'] * 6
# else:
#     shopping_list.append('milk')

# print(shopping_list)

# shopping_list = []
# mart = ['avocado', 'banana', 'milk', 'egg']
# shopping_list.append('milk')

# if "avocado" in mart:
#     shopping_list += ['avocado']

# print(shopping_list)
# print(len(shopping_list))

# numbers = [1,2,3,4,5,9,0]
# print(range(len(numbers)))

# i = 0 
# numbers = list(range(1,11))
# while i < len(numbers):
#     if numbers[i] % 2 ==0:
#         print(i)
#     i += 1

# gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1] # 1등급의 광물이 존재하는가
# print(type(len(gems)))
# i = 0
# number = 0
# while i < len(gems):
#     if gems[i] == 1:
#         number += 1
#     i += 1

# print(f'1등급의 광물이 {number}개 존재합니다. ')

# gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
# grades = {1:0, 2:0, 3:0}
# for gem in gems:
#     grades[gem] += 1
# print(grades)

# gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
# grades = [0] * 3
# for gem in gems:
#     grades[gem-1] += 1
# print(grades)

# nums = [7, 1, 2, 4, 6, 8, 3]
# i = 0
# num = nums[0]
# while i < len(nums):
#     if nums[i-1] <= num:
#         num = nums[i-1]
#         i += 1
#     else:
#         i += 1
# print(num)

# nums = [7, 1, 2, 4, 6, 8, 3]
# i = 0
# num = nums[0]
# while i < len(nums):
#     i += 1 
#     if nums[i-1] <= num:
#         num = nums[i-1]
# print(num)

# nums = [7, 1, 2, 4, 6, 8, 3]
# i = 0
# num = nums[0]
# while i < len(nums):
#     i += 1 
#     if nums[i-1] >= num:
#         num = nums[i-1]
# print(num)

# - 지금까지 학습한 random, time 모듈을 이용하여 `카운트다운이 있는 로또 번호 추첨기`를 만들어보자.
# - **추첨기는 다음과 같은 순서로 동작한다.**
#     1. 프로그램을 실행과 동시에 `5초의 카운트다운`이 진행된다. 1초가 흐를 때 마다 `“4초 남았습니다.”`와 같이 남은 시간을 출력한다.
#     2. 카운트다운이 종료되면, 1부터 45까지의 수 중 6개의 숫자를 무작위로 추출한다.
#     3. 6개의 숫자를 오름차순으로 정렬하여 출력한다.

# import random
# import time
# i = 0
# for i in range(5,0,-1):
#     print(f'"{i}초 남았습니다."')
#     time.sleep(1)
# print(sorted(random.sample(range(1,46),6)))

# matrix = [
#     [0, 5, 3, 1],
#     [4, 6, 10, 8],
#     [9, -1, 1, 5]
# ]
# print(range(len(matrix)))

# num_list = [2, 4, 5, 3, 6]
# answer = []
# for num in num_list:
#     answer.append(0)
#     if num == 2:
#         answer.pop()
#         answer.append(True)
#     else:
#         for i in range(2,num):
#             if num % i == 0:
#                 answer.pop()
#                 answer.append(False)
#                 break # 아예 이 반복을 마침
#             else:
#                 answer.pop()
#                 answer.append(True)


# print(num_)

# print(bool(3%3))

# a = 5
# i = 2
# for i in range(a):
#     if a % i != 0:
#         continue
#     answer[]
#     else:
#         continue
        