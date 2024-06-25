# 새로운 파일 만들고, hello python 출력하기.
#  프로그램 언어가 아닐 경우, 주석 처리를 해서, 컴퓨터가 인식라지 못하게 해야 합니다.
#  => 주석 crtl+/

print('Hello, python!') # Hello, python! 을 출력합니다.
print("5월 동안 잘 부탁드립니다. :) ") #  인삿말을 출력합니다.

name = input('이름을 입력해 주세요: ')
print('안녕하세요, ' + name + '님')

age = int(input('나이를 입력해 주세요: '))
next_age = age +1
print('내년에는 ' + str(next_age) + '세입니다.')