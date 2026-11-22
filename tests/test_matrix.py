from src.matrix import Matrix


def test_matrix_creation():
    A = Matrix([[1,2,3],[4,5,6]])
    assert A.data == [[1,2,3],[4,5,6]]


def test_matrix_shape():
    A = Matrix([[1,2,3],[4,5,6]])
    assert A.shape == (2,3)

def test_matrix_zero():
    A = Matrix.zero(2,4)
    assert A.data == [[0,0,0,0],[0,0,0,0]]

def test_identity():
    A = Matrix.identity(3)
    assert A.data == [[1,0,0],[0,1,0],[0,0,1]]

