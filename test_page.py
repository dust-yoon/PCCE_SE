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