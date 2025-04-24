class Product:
    
    # self --> points the current object (this)
    # __init__(self) --> constructor method that initializes fields
    
    # Constructor
    def __init__(self):
        self.name = 'LENOVO'
        self.description = 'It is a good product'
        self.price = 30000
        
    # Parameterized Constructor
    """
        
    def __init(self, id, ratings):
        self.id = id
        self.ratings = ratings
        
    """
    
    # Destructor
    def __del__(self):
        print("The destructor is called")
        
    
    # Method (or) Function
    def display(self): 
        print(self.name)
        print(self.description)
        print(self.price)
        

p1 = Product() 
p1.display()

