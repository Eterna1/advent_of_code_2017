#!/usr/bin/python3

BEGINNING_ORDER = "abcdefghijklmnop"

def swap(s, pos_a, pos_b):
    s_ = list(s)
    tmp = s_[pos_a]
    s_[pos_a] = s[pos_b]
    s_[pos_b] = tmp
    return ''.join(s_)

def dance(order, moves, moves_p = True, moves_sx = True):    
    for move in moves:
        if move[0] == "s" and moves_sx:
            #spin
            spin_num = int(move[1:])
            order = order[-spin_num:] + order[:-spin_num]
        elif move[0] == "x" and moves_sx:
            #exchange
            pos_a, pos_b = list(map(lambda x: int(x), move[1:].split("/")))
            order = swap(order, pos_a, pos_b)
        elif move[0] == "p" and moves_p:
            #partner
            letter_a, letter_b = move[1:].split("/")
            pos_a = order.find(letter_a)
            pos_b = order.find(letter_b)
            order = swap(order, pos_a, pos_b)
    
    return order

def get_positions_swaps_moves(beginning_order, ending_order):
    order = beginning_order
    moves = []
    
    for i in range(len(order)):
        if order[i] != ending_order[i]:
            pos_a = i
            pos_b = order.find(ending_order[i])
            order = swap(order, pos_a, pos_b)
            moves.append("x%d/%d" % (pos_a, pos_b))
    return moves
    

def get_letters_swaps_moves(beginning_order, ending_order):
    order = beginning_order
    moves = []
    
    for i in range(len(order)):
        if order[i] != ending_order[i]:
            pos_a = i
            pos_b = order.find(ending_order[i])
            order = swap(order, pos_a, pos_b)
            moves.append("p%s/%s" % (order[pos_a], order[pos_b]))
    return moves
    
def get_positions_swaps(moves):
    new_order = dance(BEGINNING_ORDER, moves, moves_p = False)
    return get_positions_swaps_moves(BEGINNING_ORDER, new_order)

def get_letters_swaps(moves):
    new_order = dance(BEGINNING_ORDER, moves, moves_sx = False)
    return get_letters_swaps_moves(BEGINNING_ORDER, new_order)


d_ps = {}
def apply_pswaps_many_times(positions_swaps_per_round, total_dances):
    
    if total_dances in d_ps:
        return list(d_ps[total_dances])
    
    if total_dances == 0:
        return []
    if total_dances == 1:
        return positions_swaps_per_round
    
    total_dances_a = total_dances // 2
    total_dances_b = total_dances - total_dances_a 
    
    moves_a = apply_pswaps_many_times(positions_swaps_per_round, total_dances_a)
    moves_b = apply_pswaps_many_times(positions_swaps_per_round, total_dances_b)
    
    order = BEGINNING_ORDER
    order = dance(order, moves_a)
    order = dance(order, moves_b)
        
    r = get_positions_swaps_moves(BEGINNING_ORDER, order)
    d_ps[total_dances] = tuple(r)
    
    return r

d_ls = {}    
def apply_lswaps_many_times(letters_swaps_per_round, total_dances):
    
    if total_dances in d_ls:
        return list(d_ls[total_dances])
    
    if total_dances == 0:
        return []
    if total_dances == 1:
        return letters_swaps_per_round
    
    total_dances_a = total_dances // 2
    total_dances_b = total_dances - total_dances_a 
    
    moves_a = apply_lswaps_many_times(letters_swaps_per_round, total_dances_a)
    moves_b = apply_lswaps_many_times(letters_swaps_per_round, total_dances_b)
    
    order = BEGINNING_ORDER
    order = dance(order, moves_a)
    order = dance(order, moves_b)
        
    r = get_letters_swaps_moves(BEGINNING_ORDER, order)
    d_ls[total_dances] = tuple(r)
    
    return r
    
def dance_many_times(order, moves, total_dances):
    positions_swaps_per_round = get_positions_swaps(moves)
    letters_swaps_per_round = get_letters_swaps(moves)

    positions_swaps = apply_pswaps_many_times(positions_swaps_per_round, total_dances)
    letters_swaps = apply_lswaps_many_times(letters_swaps_per_round, total_dances)

    order = dance(order, positions_swaps)
    order = dance(order, letters_swaps)
    return order
    
def dance_many_times_(order, moves, total_dances):
    for i in range(total_dances):
        order = dance(order, moves)
    return order

if __name__ == "__main__":
    moves = input().strip().split(",")
    print("part 1 - %s" % dance(BEGINNING_ORDER, moves))
    print("part 2 - %s" % dance_many_times(BEGINNING_ORDER, moves, 1000000000))
