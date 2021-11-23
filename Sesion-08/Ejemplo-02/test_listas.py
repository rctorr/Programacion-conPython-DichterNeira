import listas

def test_procesa():
    assert listas.procesa([]) == []
    assert listas.procesa([1,2,3,4,5]) == [1,2,3,4,5]
    assert listas.procesa([1,2,3,4,5,2,4,1]) == [1,2,3,4,5]
    assert listas.procesa([1,1,1,1,1]) == [1]
    assert listas.procesa([7,2,9,3,0,1,8,2]) == [0,1,2,3,7,8,9]

