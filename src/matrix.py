class Matrix:

    def __init__(self, data):
        self.data = data

    # ========================================================================
    # Generating a zero matrix with a user-defined size in used in certain matrix operations,
    # such as matrix multiplication of the generation of identity matrices.
    # ========================================================================

    @property
    def nb_lines(self):
        return len(self.data)

    @property
    def nb_colomns(self):
        return len(self.data[0]) 

    @property
    def is_zero(self):
        for n in range(self.nb_lines) :
            for m in range(self.nb_colomns) :
                if self.data[n][m] != 0 :
                    return False
        return True

    @property
    def is_square(self): 
        return len(self.data) == len(self.data[0])

    @property
    def is_empty(self):
        if self.nb_lines == 0 or self.nb_colomns == 0 :
            return True
        return False

    @property
    def is_identity(self):
        if not self.is_square :
            return False
        for n in range(self.nb_lines) :
            for m in range(self.nb_colomns) :
                if n == m and self.data[n][m] != 1 :
                    return False
                elif n != m and self.data[n][m] != 0 :
                    return False
        return True
    
    @classmethod
    def zero(cls, nb_lines , nb_colomns ):
        return cls([[ 0 for c in range(nb_colomns)] for l in range(nb_lines)])

    @classmethod
    def identity(cls, nb_lines_colomns ):
            data = [[ 0 for c in range(nb_lines_colomns) ] for l in range(nb_lines_colomns) ]
            for i in range(nb_lines_colomns):
                 data[i][i] = 1
            return cls(data)

    def __repr__(self):
        return str(self.data)

    

    