
def bigger_guy(a,b):
  if a > b:
      return a
  elif b > a:
      return b


def test_bigger_guy():
    assert bigger_guy(1, 2) == 2
    assert bigger_guy(10, 20) == 20
    assert bigger_guy(20, 10) == 20
    assert bigger_guy(10, 30) == 30
    assert bigger_guy(2, 1) == 2
    assert bigger_guy('a', 'b') == 'b' # 'b' is greater than 'a'
    print("YOUR CODE IS CORRECT!")
    #test your code by un-commenting the line(s) below
test_bigger_guy()