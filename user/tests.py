from django.test import TestCase
import user.models
# Create your tests here.


def test_insert():
    user.models.insert('마이콜', 'micol@gmail.com', '1234', 'male')


def test_fetch():
    result = user.models.fetchone(email='micol@gmail.com', password='1234')
    return result


#test_insert()
user.models.update(4,'코코넛','1234','male')