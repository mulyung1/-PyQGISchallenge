'''Task 2: Create our car using Car() custom class'''

class Car():
    
    model='Land Cruiser'
    
    def __init__(self, color, type):
        self.color=color
        self.type=type
        self.started =False
        self.stopped=False
    
    #custom functions
    def start(self):
        print('Car started')
        self.started=True
        self.stopped=False
    
    def stop(self):
        print('Car Stopped')
        self.stopped=True
        
#build our car
car1=Car('black','automatic')
#build another car
car2=Car('red','manual')

#start/use car2
car2.start()

#check color of car2 and 1
print(car2.color)
print(car1.color)


