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
        if self.data == [] :
            return 0
        else :
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
        return self.nb_lines == self.nb_colomns

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
        if not isinstance(nb_lines, int) or not isinstance(nb_colomns, int):
            raise TypeError("numbers of lines and colomns must be integers")

        if nb_lines < 0 or nb_colomns < 0:
            raise ValueError("Dimensions cannot be negative")
        
        return cls([[ 0 for c in range(nb_colomns)] for l in range(nb_lines)])

    @classmethod
    def identity(cls, nb_lines_colomns):
            data = cls.zero(nb_lines_colomns,nb_lines_colomns).data
            for i in range(nb_lines_colomns):
                 data[i][i] = 1
            return cls(data)

    def __repr__(self):
        return str(self.data)

    

    