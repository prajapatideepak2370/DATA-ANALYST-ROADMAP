class student:
    def __init__(self, phy, python, ml, ds):
        self.phy = phy
        self.python = python
        self.ml = ml
        self.ds = ds

    @property   #@property is a decorator that lets you define a method but access it like an attribute (variable) instead of calling it like a function.
    def percentage(self):
        return str((self.phy + self.python + self.ml + self.ds) / 4) + "%"
        
st1 = student(78, 89, 93, 95)
st1.python = 10
print(st1.percentage)
