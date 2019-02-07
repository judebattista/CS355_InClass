chk = { 'A':False, 'C':True, 'G':True, 'T':False }
s = "ATCTGTATAACGAATATATACATTATC"
filtered_s = ''.join(filter( lambda c: chk[c] , s ))
print( filtered_s )

