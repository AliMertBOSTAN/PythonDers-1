# Procedural light switch
def turnOn():
    global switchIsOn
    switchIsOn = True
def turnOff():
    global switchIsOn
    switchIsOn = False

switchIsOn = False #


# object-oriented programming

class LightSwitch():
    def __init__(self):
        self.switchIsOn = False # self'ler sayasinden aynı class'lardan oluşturulduğunda bu metotoların karışmasını engelliyor
    def turnOn(self):
        self.switchIsOn = True
    def turnOff(self):
        self.switchIsOn = False
    def show(self):
        print(self.switchIsOn)

# from objbrowser import browser
# objeleri incelemek için kullanılan bir kütüphane

class Circle2:
    pass

my_circle = Circle2()
my_circle.radius = 5
print('CemberinAlanı:',3.14*my_circle.radius**2)

# böyle olması daha sağlıklı
class Circle:
    def __init__(self, r=1): # bu class'ı kullanılarak oluşturulan obje
        """Create a Circle with the given radius"""
        self.radius = r
        self.__class__._all_circles.append(self)

    def __str__(self): # print ettiğimiz zaman yazdırılan
        return ' r: ' + str(self.radius)
    
    def __repr__(self): # class çağrıldığında yazdırılan
        return 'Circle(r = {0.radius!r})'.format(self)
    
    def __add__(self, other): # bu class'ın sağdaki değerle toplanmasını sağladık
        if type(other) is Circle:
            return Circle(self.radius + other.radius)
        else:
            print('Unsupported object for adding: Both object must be Circle')

    def __radd__(self, other): # bu class'ın sağdaki değerle toplanmasını sağladık
        if type(other) is Circle:
            return Circle(self.radius + other.radius)
        else:
            print('Unsupported object for adding: Both object must be Circle')

my_circle = Circle(6)
print(2 * 3.14 * my_circle.radius)