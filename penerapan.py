print('Raihan Febriahdi')
print('1E, Informatika')

def hitung_kecepatan():
   print("hitung kecepatan ready!")
   jarak = int(input("masukkan jarak: "))
   waktu = int(input("masukkan waktu: "))
   kecepatan = jarak * waktu
   print("kecepatan: ", kecepatan, "\n")

def luas_segitiga():
   print("hitung segitiga ready!")
   alas = float(input("masukkan alas: "))
   tinggi = float(input("masukkan tinggi: "))
   luas = 0.5 * (alas * tinggi)
   print("luas segitiga adalah: ", luas, "\n")

def luas_balok():
   print("hitung balok ready!")
   panjang = float(input("masukkan panjang: "))
   lebar = float(input("masukkan lebar: "))
   tinggi = float(input("masukkan tinggi: "))
   luas = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
   print("luas balok adalah: ", luas, "\n")  

while True:
   userInput = int(input(
      "Opsi pilihan rumus: \n\n1. hitung kecepatan\n2. luas segitiga\n3. luas balok\n\nopsi pilihan: "))
   if(userInput == 1):
      hitung_kecepatan()
   elif(userInput == 2):  
      luas_segitiga()
   elif(userInput == 3) :
      luas_balok()  
   else:
      break     