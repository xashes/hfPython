from chapter05 import record

def test_sanitize():
    assert record.sanitize('2:38') == '2.38'
    assert record.sanitize('2-38') == '2.38'
