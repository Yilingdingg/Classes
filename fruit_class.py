class Fruit: 
    def __init__(self, name, size, color, shape, taste, rank):
        self.name=name
        self.size=size
        self.color=color
        self.shape=shape
        self.taste=taste
        self.rank=rank
    def print_details(self):
        print("The name of the fruit is", self.name,".")
        print("The size of the fruit is", self.size,".")
        print("The shape of the fruit is", self.shape,".")
        print("The", self.name,"tastes",self.taste,".")
        print("The ranking of the fruit is", self.rank,".")
    def set_shape(self):
        self.shape=input("The shape of the fruit:")
    def get_shape(self):
        print("The shape of the", self.name, "is", self.shape, ".")
    def set_ranking(self):
        self.rank=input("The ranking of the fruit:")
    def get_ranking(self):
        print("The ranking of the fruit is now:", self.rank,".")

apple=Fruit("apple","10x10cm","red","round","sweet or sour", "2#")
banana=Fruit("banana","20x5","yellow","rectangular","sweet","3#")
mango=Fruit("mango","15x8","red, orange, and yellow","oval","sweet","1#")

apple.print_details()
apple.set_ranking()
apple.get_ranking()

mango.print_details()
