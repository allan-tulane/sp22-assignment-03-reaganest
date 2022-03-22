# assignment-03

# no other imports needed
from collections import defaultdict
import math

### PARENTHESES MATCHING

#### Iterative solution
def parens_match_iterative(mylist):
  i = iterate(parens_update, 0, mylist)
  if (i == 0):
    return True
  else:
    return False
    pass


def parens_update(current_output, next_input):
  
  if (next_input == "("):
    current_output += 1
  elif (current_output < 1 and next_input == ")"):
    current_output = -2
  elif (next_input == ")"):
    current_output -= 1
  return current_output

  
    
def iterate(f, x, a):
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])
      
def test_parens_match_iterative():
    assert parens_match_iterative(['(', ')']) == True
    assert parens_match_iterative(['(']) == False
    assert parens_match_iterative([')']) == False


#### Scan solution
def parens_match_scan(mylist):
    for i in list(map(lambda x:paren_map(x), mylist)):
        if i == -1:
            return False
        if i == 1:
            break
    red = reduce(min_f, 0,(scan(plus, 0, list(map(lambda x:paren_map(x), mylist)))[0]))
    if red == 0:
        return True
    if red !=0:
        return False
    else:
      return True
    pass
  
def scan(f, id_, a):
    """
    This is a horribly inefficient implementation of scan
    only to understand what it does.
    We saw a more efficient version in class. You can assume
    the more efficient version is used for analyzing work/span.
    """
    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )
      
def reduce(f, id_, a):
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        res = f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))
        return res
      
def paren_map(x):
    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0
def min_f(x,y):
    """
    Returns the min of x and y. Useful for `parens_match_scan`.
    """
    if x < y:
        return x
    return y

def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False

#### Divide and conquer solution

def parens_match_dc(mylist):
    """
    Calls parens_match_dc_helper. If the result is (0,0),
    that means there are no unmatched parentheses, so the input is valid.
    
    Returns:
      True if parens_match_dc_helper returns (0,0); otherwise False
    """
    # done.
    n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
    return n_unmatched_left==0 and n_unmatched_right==0

def parens_match_dc_helper(mylist):
   
    if len(mylist) == 1 and mylist[0] == ")":
        return (1, 0)
    elif len(mylist) == 1 and mylist[0] == "(":
        return (0, 1)
    elif len(mylist) == 1:
        return (0,0)
    elif len(mylist) == 0:
        return (0, 0)
    else:
        n = len(mylist)//2
        (TWO_R, RL) = parens_match_dc_helper(mylist[n:])
        (LR, TWO_L) = parens_match_dc_helper(mylist[:n])
        if TWO_L == 0 and TWO_R == 0 and LR > 0 and RL > 0:
          return (LR, RL)
        x = TWO_R - TWO_L
        y = RL - LR
        return (x, y)
    pass
  
def test_parens_match_dc():
  assert parens_match_dc(['(', ')']) == True
  assert parens_match_dc(['(']) == False
  assert parens_match_dc([')']) == False
  
def plus(x,y):
  return x + y