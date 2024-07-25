def solution(snippet, message):
    answer = ''
    snip = {}

    message = message + ' '

    for i in range(len(snippet)):
        snip[str(snippet[i][0])] = snippet[i][1]
    
    for i in range(len(snip)):
        if message.find(list(snip.keys())[i] + " ") == -1:
            continue
        else:
            message = message.replace(list(snip.keys())[i] + " " , snip[list(snip.keys())[i]] + " ")

    message.strip(message[len(message)-1])

    return message

print(solution([["msg", "message"], ["m", "me"], ["s", "see"], ["g", "group"]], "msg"))
print(solution([["IMO", "In my opinion"]], "IMO, IMO"))
print(solution([["IMO,", "In my opinion,"], 
                ["AYS?", "Are you serious?"], 
                ["TTYL.", "Talk to you later."]], 
                "IMO, it does not look so good. AYS? TTYL."))

print("In my opinion, it does not look so good. Are you serious? Talk to you later.")

# 띄어쓰기 추가해야함
# 자료형 변환
# 라이브러리, 리스트, 등등 변환과 내장 함수 파악
# 오답 정리

# snip = {'m' : 'me'}

