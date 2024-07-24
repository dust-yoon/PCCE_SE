# 머쓱이는 '생명 게임'이라고 알려진 프로그램을 만들려고 합니다. 생명 게임은 2차원 보드에서 이루어지며, 각각의 칸은 0이 저장된 죽은 칸이거나 1이 저장된 살아있는 칸입니다. 이때 자기 자신의 값과 주변 이웃한 칸들의 값에 따라 다음 세대에서 각 칸의 값이 정해집니다.

# 머쓱이가 만든 생명 게임의 규칙은 다음과 같습니다.

# # 살아있는 칸 주변에 이웃이 2명 이하로 존재하면 그 칸은 다음 세대에 죽는다
# # 살아있는 칸 주변에 이웃이 5명 이상 존재하면 그 칸은 다음 세대에 죽는다
# # 죽어있는 칸 주변에 이웃이 정확히 2명 존재하면 그 칸은 다음 세대에 살아난다.
# # 그 이외의 경우에는 살아있거나 죽은 상태가 유지된다.

# 검사 할 점의 개수n과 처음 보드의 상태 board,
# 점의 좌표를 나타내는 정수쌍 [a,b]가 n개 담긴 리스트 position이 주어졌을 때,
# 한세대 뒤에 board[a][b] 칸의 상태 리스트를 return하는 함수를 완성해주세요.

# 내 답
def solution(n, board, position):
    answer = []
    i = 0
    j = 0
    t = 0

    for i in range(n):
        # a = int(board[int(position[i][0])][0])
        a = int(position[i][0])
        b = int(position[i][1])

        total = (-1)*int(board[a][b])
        for t in range(3):
            for j in range(3):
                if int(a-1+t) <= len(board)-1 and int(b-1+j) <= len(board[0])-1:
                    total += int(board[a-1+t][b-1+j])
                else:
                    continue

        if board[a][b] == 1:
            if total <= 2 or total >= 5:
                a = 0
            else:
                a = 1
        elif board[a][b] == 0:
            if total == 2:
                a = 1
            else:
                a = 0
        
        answer.append(a)

    return answer
# 추가 답
def solution(n, board, position):
    answer = []
    for i in range(n):
        x = position[i][0]
        y = position[i][1]
        neighbor = 0

        if x != 0:
            # 왼쪽 위
            if y != 0:
                if board[x-1][y-1]:
                    neighbor += 1
            # 위
            if board[x-1][y]:
                neighbor += 1
            # 오른쪽 위
            if y != len(board[0]) -1:
                if board[x-1][y+1]:
                    neighbor += 1

        # 왼쪽
        if y != 0:
            if board[x][y-1]:
                neighbor += 1
        # 오른쪽
        if y != len(board[0]) - 1:
            if board[x][y+1]:
                neighbor += 1

            if x != len(board) - 1:
                # 왼쪽 아래
                if y != 0:
                    if board[x+1][y-1]:
                        neighbor += 1
                # 아래
                if board[x+1][y]:
                    neighbor += 1    
                # 오른쪽 아래
                if y != len(board[0]) - 1:
                    if board[x+1][y+1]:
                        neighbor += 1

            if board[x][y]:
                if 3 <= neighbor <= 4:
                    answer.append(1)
                else:
                    answer.append(0)
            else:
                if neighbor == 2:
                    answer.append(1)
                else:
                    answer.append(0)

    return answer
# 동료 답
def solution(n, board, position):
    answer = []
    xx = len(board)
    yy = len(board[0])
    
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]
    
    for i in range(len(position)) : 
        x = position[i][0]
        y = position[i][1]
        death = 0
        live = 0
        
        for j in range(8) :
            nx = x + dx[j]
            ny = y + dy[j]

            if 0 <= nx < xx and 0 <= ny < yy:
                if board[nx][ny] == 0:
                    death += 1
                else:
                    live += 1
                    
        a = position[i][0]
        b = position[i][1]

        if board[a][b] == 1:
            if live <= 2 or live >= 5:
                answer.append(0)
            else:
                answer.append(1)
        else:
            if live == 2:
                answer.append(1)
            else:
                answer.append(0)

    return answer
#동료 답_2
def solution(n, board, position):
    answer = []
    h = len(board)
    w = len(board[0])
    for i in range(len(position)):
        c = 0
        y = position[i][0]
        x = position[i][1]
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy == 0 and dx == 0:
                    continue
                if 0 <= y + dy < h and 0 <= x + dx < w:
                    if board[y + dy][x + dx] == 1:
                        c += 1
        if board[y][x] == 1:
            if c <= 2 or 5 <= c:
                r = 0
            else:
                r = board[y][x]
        else:
            if c == 2:
                r = 1
            else:
                r = board[y][x]
        answer.append(r)
    return answer

print(solution(2, [ [0, 1, 0, 0]
                   ,[1, 1, 1, 0],
                    [0, 1, 0, 1],
                    [0, 1, 0, 1],
                    [1, 1, 1, 0],
                    [0, 0, 0, 1]], [[1,3],[5,3]]))