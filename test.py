#보드는 1차원 리스트로 구현함
game_board = [' ', ' ', ' ',
              ' ', ' ', ' ',
              ' ', ' ', ' ']

#비어 있는 칸을 찾앙서 리스트로 반환함
def empty_cells(board):
    cells = []     #빈 칸 리스트
    for x, cell in enumerate(board):   #보드를 순환하며 빈칸을 찾음
        if cell == ' ':  #빈 칸 확인
            cells.append(x)   #빈 칸 인덱스 추가
    return cells  #빈 칸 리스트 반환

#비어 있는 칸에 놓을 수 있는지 확인함
def valid_move(x):
    return x in empty_cells(game_board)  #빈 칸에 두는지 여부 반환

#특정 위치 x에 플레이어의 말을 놓음
def move(x, player):
    if valid_move(x):  #유효한 위치인지 확인함
        game_board[x] = player  #해당 위치에 플레이어의 말을 놓음
        return True  #유효한 이동임을 반환함
    return False  #유효하지 않음을 반환함

#현재 게임 보드를 그림
def draw(board):
    for i, cell in enumerate(board):  #보드의 각 칸을 순회함
        if i % 3 == 0:  #3칸마다 줄을 그음
            print('\n---------------')
        print('|', cell, '|', end='')  #칸을 출력함
    print('\n---------------')  #마지막 줄을 그음

#보드 상태를 평가함
def evaluate(board):
    if check_win(board, 'X'):  #X가 이긴 경우
        score = 1  #X 승리 시 점수
    elif check_win(board, 'O'):  # O가 이긴 경우
        score = -1 #O 승리 시 점수
    else:
        score = 0  #비긴 경우
    return score  #점수 반환

#주어진 플레이어가 이겼는지 확인함
def check_win(board, player):
    win_conf = [  #승리조건
        [board[0], board[1], board[2]],  #첫 번째 행
        [board[3], board[4], board[5]],  #두 번째 행
        [board[6], board[7], board[8]],  #세 번째 행
        [board[0], board[3], board[6]],  #첫 번째 열
        [board[1], board[4], board[7]],  #두 번째 열
        [board[2], board[5], board[8]],  #세 번째 열
        [board[0], board[4], board[8]],  #대각선(좌상단->우하단)
        [board[2], board[4], board[6]]  #대각선(우상단->좌하단)
    ]
    return [player, player, player] in win_conf  #승리 여부 반환

#게임이 끝났는지 확인함
def game_over(board):
    return check_win(board, 'X') or check_win(board, 'O')  #승리 여부 확인

#미니맥스 알고리즘을 구현함
#이 함수는 재귀적으로 호출됨
def minimax(board, depth, alpha, beta, maxPlayer):
    pos = -1  #최적 위치 초기값 설정
    #단말 노드이면 보드를 평가하여 위치와 평가값을 반환함
    if depth == 0 or len(empty_cells(board)) == 0 or game_over(board):
        return -1, evaluate(board)  #단말 노드에서 점수 반환

    if maxPlayer:  #최대화하는 플레이어의 경우
        value = -10000  #음의 무한대
        #자식 노드를 하나씩 평가하여서 최선의 수를 찾음
        for p in empty_cells(board):  #빈 칸마다
            board[p] = 'X'  #X를 놓음

            #경기자를 교체하여서 minimax를 재귀적으로 호출함
            x, score = minimax(board, depth - 1, alpha, beta, False)
            board[p] = ' '  #보드를 원래 상태로 돌림
            if score > value:
                value = score  #최대값 갱신
                pos = p  #최적 위치 저장
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
    else:  #최소화하는 플레이어의 경우
        value = +10000  #양의 무한대
        #자식 노드를 하나씩 평가하여서 최선의 수를 찾음
        for p in empty_cells(board):  #빈 칸마다
            board[p] = 'O'  #O를 놓음

            #경기자를 교체하여서 minimax를 재귀적으로 호출함
            x, score = minimax(board, depth - 1, alpha, beta, True)
            board[p] = ' '  #보드를 원래 상태로 돌림
            if score < value:
                value = score  #최소값 갱신
                pos = p  #최적 위치 저장
                beta = min(beta, value)
                if beta <= alpha:
                    break
    return pos, value  #위치와 을 반환함

player = 'X'  #플레이어 설정

#메인 프로그램 루프
while True:
    draw(game_board)  #보드 상태 출력
    if len(empty_cells(game_board)) == 0 or game_over(game_board):  #게임 종료 여부 확인
        break #게임종료
    i, v = minimax(game_board, 9, -10000, 10000, player == 'X')  #미니맥스 알고리즘으로 최적 수 계산
    move(i, player)  #최적 위치에 수를 둠
    if player == 'X':  #플레이어 교체
        player = '0'
    else:
        player = 'X'

#게임 종료 시 결과 출력
if check_win(game_board, 'X'):
    print('X 승리!')
elif check_win(game_board, '0'):
    print('0 승리!')
else:
    print('비겼습니다!')
