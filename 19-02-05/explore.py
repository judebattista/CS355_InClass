# comments are cool and necessary!
print("Hello Bioinformatics")

name = "beta"
# .fa is FASTA file format
name = name + "globin" + ".fa"

print(name)

# we can repeat strings using the * operator
tandem_repeat = 3 * "ATTCG"
print(tandem_repeat)

#to get the length of a string use len()
name_length = len(tandem_repeat)

# .upper() and .lower() set the case of a string
upperName = name.upper()
print("Upper case name: " + upperName)
print("Original name: " + name)

# We can access parts of strings, but not change them
# Strings are immutable in Python
print('The fourth character in upperName is ' + upperName[3])
#name[3] = 'B' # Would throw an error

name = 'ATCGGGTTTAAACGTA'
print(name[3])
# We can slice out parts of a string
print('------------------------')
print(name)         # output whole string
print(name[3:5])    # output the 4th and 5th chars 'GG'
print(name[3:])     # output the 4th char to the end
print(name[:5])     # output the 1st char to the 5th char 'ATCGG'
print('------------------------')
print(name[5:3:-1])     # output the 6th and 5th chars in reverse order 'GG'
# that wasn't very interesting, so let's try another section
print(name[3:1:-1])     # output the 4th and 3rd chars in reverse order 'GC'
print(name[5::-1])      # output the sixth char to the beginning in reverse order
print(name[:3:-1])      # start at the end and print through the fifth char
print(name[::-1])       # print whole string in reverse order
print('------------------------')

def reverse(s):
    return s[::-1]

# code before call to reverse
val = reverse("this was forward")
print(val)
# code after the call to reverse
print(reverse(val))

# We can use loops to access parts of a string computationally
# Example: generate all possible codons
# Since each codon is three chars, there are three possible frames, depending where we start
# A special start codon indicates where we should start, but we may not know it
s = 'ATCGATAGACGACGAAGAG'
for i in range(len(s) - 3 + 1):
    kword = s[i:i+3]
    print(kword)

# three ways to store sequences of data
myList = ['a', 'b', 'c']
myDictionary = {'a':1, 'b':True, 'c':'name'}
myTuple = ('a', 'b', 'c')

# unlike strings, lists are mutable
print('------------------------')
print(myList)
myList.append('d')
myList.append('e')
myList.append('f')
print(myList)
# we can access list items by their index
# and we can slice lists using indices
print('------------------------')
print("Slicing lists:")
print('------------------------')
print(myList[1])
print(myList[2:5])
print(myList[2:])
print(myList[:5])
print('------------------------')
print(myList[5:2:-1])
print(myList[5::-1])
print(myList[:3:-1])
print(myList[::-1])
print('------------------------')

catch = 'nothin'
# we can remove items from a list either by position or by value
catch = myList.pop(2)           # removes the item at index 2 and returns it
print(myList)
print(catch)
catch = myList.remove('b')      # removes the first item with value 'b' but does NOT return it
print(myList)
print(catch)
print('------------------------')

# we can concatenate lists using +
more_list = ['k', 'j', 'i', 'h', 'g']
all_list = myList + more_list
print(all_list)
print('------------------------')

# it is also easy to sort lists in python
all_list.append('c')
all_list.append('b')
sorted_list = sorted(all_list)
print(sorted_list)
print('------------------------')
print('Printing items in all_list:')
print('------------------------')
for item in sorted_list:
    print('element: ' + item)
print('------------------------')
print('Getting the index for each item')
print('------------------------')
for ndx, item in enumerate(sorted_list):
    print('element ' + str(ndx) + ': ' + item)
print('------------------------')

# Dictionaries are the best
# They function as translators. For example, we can translate DNA to RNA
baseComp = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
s = 'ATCGATGATACATAGACTATGGGGGCCTTA'
scomp = ''      # We'll add this line to define scomp in the correct even though we apparently do not need to
complementS = []
for base in s:
    complementS.append(baseComp[base])
    scomp = ''.join(complementS)        # This should be out of scope when we print but it is not! Why?
print(s)
print(scomp)
print('------------------------')
# Now let's do it with a function!
def complement(s):
    baseComp = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    letters = []
    for base in s:
        letters.append(baseComp[base])
    returnStr = ''.join(letters)
    return returnStr
print('Function version')
print('------------------------')
acids = 'AAATTTTTGGGGCCCC'
print(acids)
print(complement(acids))
print('------------------------')
