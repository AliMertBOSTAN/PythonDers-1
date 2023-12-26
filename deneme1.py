import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2 + 4*x + 4  # Örnek bir fonksiyon (x^2 + 4x + 4)

# Arama aralığını ve adım büyüklüğünü tanımla
a = -10  # Arama aralığının başlangıç noktası
b = 10   # Arama aralığının bitiş noktası
step = 0.1  # Adım büyüklüğü

# Başlangıçta minimum değeri sonsuz olarak ayarla
min_value = float('inf')
min_point = None

# Arama aralığını dolaş
current_point = a
iteration_count = 0

while current_point <= b:
    # Fonksiyon değerini hesapla
    current_value = f(current_point)
    
    # Minimum değeri güncelle
    if current_value < min_value:
        min_value = current_value
        min_point = current_point

    # Bir sonraki noktaya ilerle
    current_point += step
    
    # Iterasyon sayısını artır
    iteration_count += 1

print(f"Belirli İterasyon Sayısı ({iteration_count}) ile Minimum Nokta: {min_point}")
print(f"Belirli İterasyon Sayısı ({iteration_count}) ile Minimum Değer: {min_value}")

# Fonksiyon grafiğini çiz
x_values = np.linspace(a, b, 400)
y_values = f(x_values)

plt.plot(x_values, y_values, label='f(x) = x^2 + 4x + 4', color='blue')
plt.scatter(min_point, min_value, color='red', label=f'Minimum Nokta: {min_point}')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Fonksiyon Grafiği ve Minimum Nokta')
plt.legend()
plt.grid(True)

# Grafiği göster
plt.show()
