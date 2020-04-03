import sys
for i in range(1, 9):
    for j in range(1, 9):
        if(i + j) % 2 == 0:
            sys.stdout.write(chr(219))
            sys.stdout.write(chr(219))
        else:
            sys.stdout.write('  ')
    print('')
