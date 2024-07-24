def solution(serial):
    answer = ''
    gender = serial[:2]
    depart = serial[2:4]
    team = serial[4:6]
    vaild = serial[6:]
    
    info = {
        '01':'male',
        '02':'female',
        '10':'operation',
        '11':'sales',
        '12':'develop',
        '13':'finance',
        '14':'law',
        '15':'research'
    }

    answer += info[gender]
    answer += '/'
    answer += info[depart]
    answer += '/'
    answer += str(int(team)) + 'team'
    answer += '/'

    total = 0
    i = 0
    for i in serial[:6]:
        total += int(i)
    if total % 13 == int(vaild):
        answer += 'valid'
    else:
        answer += 'invalid'

    return answer

solution('01121344')
print(solution('01121344'))

#  문자열, 리스트, 숫자형 공부 필요함