with open('julie.txt') as fh:
    julie_records = fh.readline().strip().split(',')

julie = sorted(julie_records)
print(julie)
