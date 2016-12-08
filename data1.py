import os

if os.path.exists('sketc.txt'):
    with open('sketch.txt') as f:
        for line in f:
            if line.find(':') != -1:
                (role, line_spoken) = line.split(':', maxsplit=1)
                print('{0} said: {1}'.format(role, line_spoken), end='')
            else:
                print(line, end='')
else:
    print("The data file is missing!")
