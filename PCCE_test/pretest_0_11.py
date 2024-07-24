def solution(X, Y):
    answer = ''
    num_X = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    num_Y = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for i in list(X):
        num_X[int(i)] += 1
    for i in list(Y):
        num_Y[int(i)] += 1
    
    for i in range(10):
        if num_X[i] >= num_Y[i]:
            num_X.pop(i)
            if num_Y[i] == 0:
                num_Y.pop(i)

        else:
            num_Y.pop(i)
            if num_X[i] == 0:
                num_X.pop(i)
    
    num_X.update(num_Y)
    num = num_X

    if bool(num) == False:
        answer = '-1'
    elif len(num) == 1 and list(num.keys())[0] == 0:
        answer = '0'
    else:
        for i in range(len(list(num))):
            answer += str(max(num))*num[max(num)]
            num.pop(max(num))

    return answer

print(solution('100', '203045'))