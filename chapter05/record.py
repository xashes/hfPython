# def get_data(athlete):
    # with open('{}.txt'.format(athlete)) as fh:
        # records = fh.readline().strip().split(',')
    # return records

def sanitize(time_string):
    if ':' in time_string:
        splitter = ':'
    elif '-' in time_string:
        splitter = '-'
    else:
        return time_string
    return time_string.replace(splitter, '.')

def test_sanitize():
    assert sanitize('2:38') == '2.38'
    assert sanitize('2-38') == '2.38'
