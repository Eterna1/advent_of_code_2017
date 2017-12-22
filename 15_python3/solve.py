#!/usr/bin/python3


def solve(A, B, pairs_to_consider):
    factor_A = 16807
    factor_B = 48271
    modulo = 2147483647
    final_count = 0
    
    for i in range(pairs_to_consider):
        A = A * factor_A % modulo
        B = B * factor_B % modulo
    
        if A & 0xFFFF == B & 0xFFFF:
            final_count += 1
            
    return final_count

def solve2(A, B, pairs_to_consider):
    factor_A = 16807
    factor_B = 48271
    modulo = 2147483647
    final_count = 0
    
    for i in range(pairs_to_consider):
        A = A * factor_A % modulo
        while A & 3:
            A = A * factor_A % modulo
            
        B = B * factor_B % modulo
        while B & 7:
            B = B * factor_B % modulo
    
        if A & 0xFFFF == B & 0xFFFF:
            final_count += 1
            
    return final_count


if __name__ == "__main__":
    assert (solve(65, 8921, 5) == 1)
    print(solve(873, 583, 40000000))
    assert (solve2(65, 8921, 5000000) == 309)
    print (solve2(873, 583, 5000000))
