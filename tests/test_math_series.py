from math_series import __version__
from math_series.series import fibonacci,lucas,sum_series

def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci_0():
      actual = fibonacci(0)
      expected = 0
      assert actual == expected


def test_licas_0():
      actual = lucas(0)
      expected = 2
      assert actual == expected

def test_sum_series_0():
      actual = lucas(0)
      expected = 2
      assert actual == expected



def test_fibonacci_1():
      actual = fibonacci(1)
      expected = 1
      assert actual == expected


def test_licas_1():
      actual = lucas(1)
      expected = 1
      assert actual == expected

def test_sum_series_1():
      actual = sum_series(1)
      expected = 1
      assert actual == expected



def test_fibonacci_2():
      actual = fibonacci(2)
      expected = 1
      assert actual == expected


def test_licas_2():
      actual = lucas(2)
      expected = 3
      assert actual == expected

def test_sum_series_2():
      actual = sum_series(2)
      expected = 1
      assert actual == expected



def test_sum_series_2_3_4():
      actual = sum_series(2,3,4)
      expected = 10
      assert actual == expected