i = 10
for i in range(10):
    for j in range(10):
        if j < i:
            print(chr(219), end='')
            print(chr(219), end='')
        else:
            print(' ', end='')
    print()
