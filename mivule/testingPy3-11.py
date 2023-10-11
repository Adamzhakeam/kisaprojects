def getSquare(n:float|int) -> float:
    '''
    this function calculates the square of the argument. 
    the argument itself is not changed
    '''
    return float(n)*n

for value,answer in [(1,1), (2,4), (3,9.0), (4,16)]:
    assert getSquare(value)==answer, f"failed test for arg `{value}`"
print('all went well!!')