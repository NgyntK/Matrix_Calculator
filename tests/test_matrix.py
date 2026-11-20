from src.matrix import Matrix


def test_matrix_creation():
    A = Matrix([[1, 2], [3, 4]])
    assert A.data == [[1, 2], [3, 4]]


def test_matrix_shape():
    A = Matrix([[1, 2, 3], [4, 5, 6]])
    assert A.shape == (2, 3)