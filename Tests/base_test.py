import pytest

from Application import App

teststr = "Hello"


def setUp():
    teststr = "Hello2"


def test():
    assert 'test'.upper() == 'TEST'


def testHello():
    assert 'Hello' == teststr


def testApp():
    print(App.hellostring)
