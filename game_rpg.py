class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

    #  method serang di dalam class
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    # method diserang di dalam class
    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")


# -- Main Program --
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

print("\n--- Pertarungan Dimulai ---")
hero1.serang(hero2)
hero2.serang(hero1)

# Class Mage adalah anak dari class Hero
class Mage(Hero):
 def __init__(self, name, hp, attack_power, mana):
 # Memanggil constructor milik Parent (Hero)
   super().__init__(name, hp, attack_power)
   self.mana = mana
 def info(self):
   print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")

class Hero:
    def __init__(self, name, hp_awal, attack_power):
        self.name = name
        self.attack_power = attack_power
        # Enkapsulasi: HP bersifat private
        self.__hp = hp_awal

    # GETTER
    def get_hp(self):
        return self.__hp

    # SETTER
    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def info(self):
        print(f"Hero: {self.name} | HP: {self.get_hp()} | Power: {self.attack_power}")

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def diserang(self, damage):
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.get_hp()}")


# ===== CLASS ANAK =====
class Mage(Hero):
    def __init__(self, name, hp_awal, attack_power, mana):
        super().__init__(name, hp_awal, attack_power)
        self.mana = mana

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.get_hp()} | Mana: {self.mana}")


# ===== MAIN PROGRAM =====
hero1 = Hero("Layla", 100, 15)
hero2 = Mage("Eudora", 80, 30, 100)

print("\n--- Pertarungan Dimulai ---")
hero1.serang(hero2)
hero2.serang(hero1)

print("\n--- Uji Enkapsulasi ---")
hero1.set_hp(-50) 
print(hero1.get_hp())

from abc import ABC, abstractmethod

# ===== ABSTRACT CLASS =====
class GameUnit(ABC):

    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass


# ===== CLASS KONKRET 1 =====
class Hero(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    def serang(self, target):
        print(f"Hero {self.nama} menyerang {target}!")

    def info(self):
        print(f"Saya adalah Hero: {self.nama}")


# ===== CLASS KONKRET 2 =====
class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    def serang(self, target):
        print(f"Monster {self.jenis} menyerang {target}!")

    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")


# ===== UJI COBA =====
# unit = GameUnit()  # EROR: Abstract class tidak bisa dibuat objek

h = Hero("Alucard")
m = Monster("Serigala")

h.info()
h.serang("Monster")

m.info()
m.serang("Hero")

# ===== PARENT CLASS =====
class Hero:
    def __init__(self, nama):
        self.nama = nama

    def serang(self):
        print("Hero menyerang dengan tangan kosong")


# ===== CHILD CLASS 1 =====
class Mage(Hero):
    def serang(self):
        print(f"{self.nama} (Mage) menembakkan Kilatan listrik Settt!")


# ===== CHILD CLASS 2 =====
class Archer(Hero):
    def serang(self):
        print(f"{self.nama} (Archer) memanah dari jauh! Jleb!")


# ===== CHILD CLASS 3 =====
class Fighter(Hero):
    def serang(self):
        print(f"{self.nama} (Fighter) memukul dengan pedang! Slash!")


# ===== PENERAPAN POLYMORPHISM =====
# Kita punya daftar hero campuran
pasukan = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Mage("Gord")
]

print("\n--- PERANG DIMULAI ---")

# Satu perintah, tapi respon berbeda-beda
for pahlawan in pasukan:
    pahlawan.serang()
    
    
# ===== CHILD CLASS BARU =====
class Healer(Hero):
    def serang(self):
        print(f"{self.nama} tidak menyerang, tapi menyembuhkan teman!")

pasukan = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Mage("Gord"),
    Healer("Rafaela")
]

for pahlawan in pasukan:
    pahlawan.serang()

class Archer(Hero):
    def tembak_panah(self):
        print(f"{self.nama} (Archer) menembakkan panah! Jleb!")

for pahlawan in pasukan:
    pahlawan.serang()
        