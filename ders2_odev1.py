students = []

def ekle(ad, soyad):
    students.append(f"{ad} {soyad}")

ekle("Ebru", "Yilmaz")
ekle("Adil", "Yilmaz")
ekle("Begum", "Yilmaz")

def yazdir(students):
    i=0
    while i<len(students):
        print(students[i])
        i+=1

yazdir(students)

def kaldir(ad, soyad):
    students.remove(f"{ad} {soyad}")

kaldir("Adil", "Yilmaz")
yazdir(students)

def ekle2(*ogrenciler):
    students.extend(ogrenciler)

ekle2("Emine Yilmaz", "Busra Yilmaz")

yazdir(students)

def numara (ad, soyad):
     ogrencino = students.index(f"{ad} {soyad}")
     print(ogrencino)

numara("Ebru", "Yilmaz") 
numara("Busra", "Yilmaz")

def sil(*silinecekler):
     for i in silinecekler:
         students.remove(i)

sil("Emine Yilmaz","Busra Yilmaz")

yazdir(students)