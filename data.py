import pickle

man = []
other = []
try:
    with open('sketch.txt') as f:
        for line in f:
            try:
                (role, line_spoken) = line.split(':', maxsplit=1)
                line_spoken = line_spoken.strip()
                if role == 'Man':
                    man.append(line_spoken)
                else:
                    other.append(line_spoken)
            except ValueError:
                pass
except FileNotFoundError as err:
    print(err)

try:
    with open('man_data.pickle', 'wb') as mdata, open('other_data.pickle',
                                                      'wb') as odata:
        pickle.dump(man, mdata)
        pickle.dump(other, odata)
except FileNotFoundError as err:
    print(err)
except pickle.PickleError as perr:
    print('Pickling error: {}'.format(perr))
