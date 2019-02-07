# open the file and read everything at once
'''
open flags:
    r: read (default)
    w: write, destroys current file contents
    x: exclusive creation. Fails if file exists
    a: append to end of file
    b: binary mode
    t: text mode (default)
    +: reading and writing. If you do not seek to the end, you will overwrite contents
'''    
with open('data.txt', 'r') as infile:
    data = infile.read()
    lines = [s.strip() for s in data.splitlines()]

print(lines)

with open('dataOut.txt', 'w') as outfile:
    for line in lines:
        values = line.split()
        outfile.write(values[1].strip() + ' ' + values[0].strip() + '\n')
