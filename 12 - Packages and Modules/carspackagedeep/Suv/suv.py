from cars import Car

class SUV(Car):
    def __init__(self, make, model):
        self.segment = "SUV"
        super().__init__(make, model)
        print("Init success!!")
        
    
print("I am outside the guard!")

if __name__ == "__main__":
    print("I am inside the guard!")