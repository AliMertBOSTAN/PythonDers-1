""" Keni kütüphanemizi tasarlıyoruz """ #bu bir doc string
pi = 3.1415

def area(r):
    """Bu fonksiyon r değişteki alır ve ilgli çemberin alanını verir"""
    global pi
    return pi * r * r

def arcLength(r, theta):
    return r * 0.01745 * theta

def circumference(r):
    global pi 
    return 2 * pi * r

__all__ = ['area', 'arcLength'] # bu sayede gözükmesini istemediğimiz fonksiyonları gizleyebiliriz
