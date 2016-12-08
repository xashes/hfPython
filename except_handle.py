try:
    data = open('missing.txt')
    print(data.readline(), end='')
except FileNotFoundError as err:
    print('File error: {}'.format(err))
finally:
    data.close()
