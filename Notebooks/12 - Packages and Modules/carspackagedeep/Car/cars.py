class Car:
    """Define a class that represents a real life car."""
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.gear = 0
        self.speed = 0
        
    def start(self):
        """Start the vehicle on neutral gear"""
        if self.gear==0:
            print("...VROOOOM....Started!")
        
    def shift_up(self):
        """Increment gear and speed"""
        self.gear += 1
        self.speed += 5
        
    def shift_down(self):
        """Decrease gear and speed"""
        self.gear -= 1
        self.speed -= 5
        
    def accelerate(self):
        """Increase speed"""
        self.speed += 5
                
    def check_speed_and_gear(self):
        """See the car speed"""
        print("I'm driving at:", self.speed, "in gear:", self.gear)
    
    def stop(self):
        """Apply brakes and stop. Bring to neutral gear"""
        self.speed = 0
        self.gear = 0
        
    def start_drive(self):
        """Check if vehicle is in neutral, shiift up and drive."""
        if self.gear==0:
            self.shift_up()
            print("Shift Up and Drive.")
            print("I am driving at ", self.speed, "mph")
        
    def __str__(self):
        """Controls how the class instance is printed"""
        return 'Make is ' + str(self.make) + ', Model is ' + str(self.model)
    
    def __repr__(self):
        """Controls how the class instance is shown"""
        return 'Make ' + str(self.make) + ', model: ' + str(self.model)
    
    def __call__(self):
        """Controls what happens when the class inst is caller."""
        print("Calling the function!")
        return 'Make: ' + str(self.make) + ', Model: ' + str(self.model)
    
print("__name__: ", __name__)