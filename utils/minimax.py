from utils.heuristica import score_position
import random
import math

def jogada_vencedora(board, player):
    NUM_LIN = len(board)
    NUM_COL = len(board[0])
    for i in range(NUM_LIN):
        for j in range(NUM_COL-3):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == player:
                return True
    for j in range(NUM_COL):
        for i in range(NUM_LIN-3):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == player:
                return True
    for i in range(NUM_LIN-3):
        for j in range(NUM_COL-3):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == player:
                return True
    for i in range(NUM_LIN-3):
        for j in range(3, NUM_COL):
            if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] == player:
                return True
    return False

def solta_bolinha(board, bolinha, coluna):
    linha = 0
    while linha < len(board) and board[linha][coluna] == 0:
        linha+=1
    board[linha-1][coluna] = bolinha

def isValid(board, coluna):
    return coluna >= 0 and coluna < len(board[0]) and board[0][coluna] == 0

def remove(board, coluna):
    NUM_LIN = len(board)
    i = 0
    while i < NUM_LIN and board[i][coluna] == 0:
        i+=1
    if i < NUM_LIN:
        board[i][coluna] = 0

def get_colunas_validas(board):
    colunas_validas = []
    for col in range(len(board[0])):
        if isValid(board, col):
            colunas_validas.append(col)
    return colunas_validas

def opp_player(player):
    return 1 if player == 2 else 2



def terminal(board):
    return jogada_vencedora(board, 2) or jogada_vencedora(board, 1) or len(get_colunas_validas(board)) == 0


#Minimax com Alpha Beta
def minimax2(board, depth, alpha, beta, maximazing_player):

    is_terminal = terminal(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if jogada_vencedora(board, 1):
                return None, -math.inf
            elif jogada_vencedora(board, 2):
                return None, math.inf
            else:
                return None, 0
        return None, score_position(board, 2)

    colunas_validas = get_colunas_validas(board)
    best_col = random.choice(colunas_validas)
    if maximazing_player:
        score = -math.inf
        for col in colunas_validas:
            #temp_board = [linha.copy() for linha in board]
            solta_bolinha(board, 2, col)
            new_score = minimax2(board, depth-1,alpha, beta,False)[1]
            remove(board, col)
            if new_score > score:
                score = new_score
                best_col = col
            alpha = max(alpha, score)
            if alpha >= beta:
                break
        return best_col, score
    else:
        score = math.inf
        for col in colunas_validas:
            #temp_board = [linha.copy() for linha in board]
            solta_bolinha(board, 1, col)
            new_score = minimax2(board, depth-1, alpha, beta, True)[1]
            remove(board, col)
            if new_score < score:
                score = new_score
                best_col = col
            beta = min(beta, score)
            if alpha >= beta:
                break
        return best_col, score

def get_best_move(board):
    resp = minimax2(board, 6, -math.inf, math.inf, True)
    return resp

#Minimax + Alpha Beta + Otimizações
