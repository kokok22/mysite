from django.test import TestCase

# Create your tests here.
import guestbook.models


def test_insert():
    guestbook.models.insert('보라돌이','1234','ㅊㅊㅊㅊ')


def test_delete():
    guestbook.models.delete(4,'1234')


# test_insert()
# test_delete()
result = guestbook.models.fetchlist()
print(result)