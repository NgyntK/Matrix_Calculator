class Matrix:

    def __init__(self, data):
        self.data = data #matrix

    @property
    def shape(self):
        return (len(self.data), len(self.data[0])) # ( number of line , number of colomn )