from django.test import TestCase

# Create your tests here.
import board.models


def test_fetch():
    result = board.models.fetchlist()
    return result


def test_insert():
    board.models.insert('test3', 'test_user3', '룰루랄라')

def test_fetchno():
    result = board.models.fetchno('11')
    return  result



result = board.models.selectg_no()
# result = test_fetch()
print(result)