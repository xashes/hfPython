file = open('sketch.txt', 'w')

for i in range(20):
    print('line {}'.format(i), file=file)

file.close()
