
class Addition:
    
    def add(self, x, y):
        return sum([x,y])
    
    def add(self, x, y, z): # last definition overwrites the previous one
        return sum([x,y,z])
    
    
if __name__ == "__main__":
    addition_obj = Addition()
    addition_obj.add(5,6,7)