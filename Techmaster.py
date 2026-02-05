from abc import ABC, abstractmethod

# ===== ABSTRACT CLASS =====
class Product(ABC):
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.__stok = stok   # Encapsulation (private)

    # Getter
    def get_stok(self):
        return self.__stok

    # Setter
    def set_stok(self, jumlah):
        if jumlah < 0:
            self.__stok = 0
        else:
            self.__stok = jumlah

    @abstractmethod
    def info(self):
        pass


# ===== CLASS ANAK: LAPTOP =====
class Laptop(Product):
    def __init__(self, nama, harga, stok, ram):
        super().__init__(nama, harga, stok)
        self.ram = ram

    def info(self):
        print(f"Laptop: {self.nama} | RAM: {self.ram}GB | Harga: {self.harga} | Stok: {self.get_stok()}")


# ===== CLASS ANAK: SMARTPHONE =====
class Smartphone(Product):
    def __init__(self, nama, harga, stok, kamera):
        super().__init__(nama, harga, stok)
        self.kamera = kamera

    def info(self):
        print(f"Smartphone: {self.nama} | Kamera: {self.kamera}MP | Harga: {self.harga} | Stok: {self.get_stok()}")

# ===== DATA PRODUK =====
inventaris = [
    Laptop("Asus Vivobook", 8500000, 10, 16),
    Smartphone("Samsung Galaxy A15", 2800000, 25, 50),
    Laptop("Lenovo Ideapad", 9000000, 5, 8),
    Smartphone("Xiaomi Redmi Note 13", 3200000, 20, 108)
]

print("\n=== DATA INVENTARIS TECHMASTER ===")

# Polymorphism: satu loop, banyak perilaku
for barang in inventaris:
    barang.info()
