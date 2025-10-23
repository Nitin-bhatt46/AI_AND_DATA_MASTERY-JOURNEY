class Car:
    def __init__(self, brand, model):
        self.brand = brand      # attribute
        self.model = model      # attribute
    
    def drive(self):            # method
        print(f"{self.brand} {self.model} is driving.")
