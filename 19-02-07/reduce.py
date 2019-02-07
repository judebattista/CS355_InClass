from functools import reduce
s = "ATCTGTATAACGAATATATACATTATC"
bp_counts = { 'A':0, 'C':0, 'G':0, 'T':0 }
def countit( acc, c ) :
    acc[c] += 1
    return acc

reduce( countit, s, bp_counts )
print( bp_counts )

