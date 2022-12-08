"""
Exercise 4, Task 1
Laura Kargl, 11731038
"""
import Restriction

def pattern(sequence, pattern, circ = False):
    
    List = []
    n = len(pattern)
    m = len(sequence)
    if not circ:
        for i in range(m-(n-1)):
            match = sequence[i:i + n]
            if match == pattern:
                List.append([i, i+n])
    else:
        for i in range(m):
            if i + n <= m-1:
                match = sequence[i:i + n]
                if match == pattern:
                    List.append([i, i+n])
            else: 
                match = sequence[i:i+(m-i)]
                match += sequence[0: n-(m-i)]
                if match == pattern:
                    List.append([i,  n-(m-i)])
    LoS=(Restriction.Restriction(List, m, circ))
    
    return (List, LoS)
