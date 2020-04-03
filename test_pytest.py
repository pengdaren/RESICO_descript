import pytest
import re


@pytest.mark.go
def test_1():
    print('first')


@pytest.mark.out
def test_2():
    print('secend')
    assert 10 == 1


@pytest.mark.go
def test_3():
    print('thrid')
    assert 'i' in 'because'


@pytest.mark.out
def test_4():
    print('four')
    assert 'xxx' is 'xxa'

if __name__ == '__main__':
    pytest.main('-v', '-m', 'go', 'test_pytest.py')
    re.findall()