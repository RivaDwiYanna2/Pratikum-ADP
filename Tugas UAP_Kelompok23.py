import os
import time
os.system('cls')

from termcolor import colored, cprint
for i in range(17):
    cprint(" "*155, "white", "on_light_cyan")
print(":"*58, end ='')
sapa = "        WELCOME TO A'R UNIVERSITY       "
cprint(sapa, "black", "on_light_blue", end = '')
print(":"*57, end = '')
print()
for i in range(17):
    cprint(" "*155, "white", "on_light_cyan")

time.sleep(3)
os.system('cls')

for i in range(17):
    cprint(" "*155, "black", "on_black")
print(":"*60, end ='')
print("  prepare for log in...  " , end = '')
print(":"*60)
time.sleep(2)
os.system('cls')

for i in range(17):
    cprint(" "*155, "black", "on_black")
print(":"*60, end ='')
print("  loading : 0 %  ", end = '')
print(":"*60)
time.sleep(1)
os.system('cls')

for i in range(17):
    cprint(" "*155, "black", "on_black")
print(":"*60, end ='')
print("  loading : 10 %  ", end = '')
print(":"*60)
time.sleep(3)
os.system('cls')

for i in range(17):
    cprint(" "*155, "black", "on_black")
print(":"*60, end ='')
print("  loading : 25 %  ", end = '')
print(":"*60)
time.sleep(2)
os.system('cls')

for i in range(17):
    cprint(" "*155, "black", "on_black")
print(":"*60, end ='')
print("  loading : 40 %  ", end = '')
print(":"*60)
time.sleep(3)
os.system('cls')

for i in range(17):
    cprint(" "*155, "black", "on_black")
print(":"*60, end ='')
print("  loading : 75 %  ",end = '')
print(":"*60)
time.sleep(4)
os.system('cls')

for i in range(17):
    cprint(" "*155, "black", "on_black")
print(":"*60, end ='')
print("  loading : 100 %  ", end = '')
print(":"*60)
time.sleep(2)
os.system('cls')


Email = ''
Sandi = ''
while True:
    cprint("Pilih Daftar jika Belum Memiliki Akun", "black", "on_light_green")
    cprint(" "*10, "black", "on_black")
    Pilihan = ("1. Daftar                     ")
    cprint(Pilihan, "black", "on_light_cyan")
    cprint(" "*30, "cyan", "on_light_cyan")
    cprint(" "*10, "black", "on_black")
    Pilihan = ("2. Masuk                      ")
    cprint(Pilihan, "black", "on_light_cyan")
    cprint(" "*30, "cyan", "on_light_cyan")
    Pilihan = input("Masukkan Pilihan Anda : ")

    if Pilihan == "1":
        cprint("\nSilahkan Isi Data Berikut.", "black", "on_light_green")
        Email = input ("Email      : ")
        Nama = input ("Nama       : ")
        NIM = int(input("NIM        : "))
        Sandi = input ("Kata Sandi : ")
        cprint ("\nTerimakasih Sudah Melakukan Pendaftaran.", "black", "on_light_green")
        cprint("\nSilahkan Pilih 2 untuk Masuk", "black", "on_light_green")
        time.sleep(3)
        os.system('cls')
    elif Pilihan == "2":
        if Email =='' or Sandi =='' :
            cprint("\nAnda Belum Terdaftar. Silahkan Daftar Terlebih Dahulu\n", "black", "on_light_red")
        else:
            cprint("\nMasukkan Alamat Email dan Kata Sandi Akun Anda yang Sudah Terdaftar\n", "black", "on_light_green")
            email_daftar = input ("Email      : ")
            sandi_daftar = input ("Kata Sandi : ")
            if email_daftar == Email and sandi_daftar == Sandi:
                cprint ("\nProses Masuk Berhasil", "black", "on_light_green")
                time.sleep(2)
                os.system('cls')
                break
            else:
                    cprint("\nEmail atau Sandi Anda Salah, Silahkan Coba Lagi.", "black", "on_light_green")
        time.sleep(2)
        os.system('cls')
    else :
        cprint("Pilihan Anda Tidak Valid. Silahkan Coba Lagi", "black", "on_light_green")
        time.sleep(2)
        os.system('cls')

cprint ("Welcome To A'R University", "green")    

print ('''  \nVisi A'R University :
            Universitas A'R memiliki cita-cita ideal yang ingin diwujudkan di masa yang akan datang, 
            melalui visi Universitas A'R yaitu :
            “Menjadi Universitas Terbaik di Indonesia ”
       ''')
print (''' \nMisi A'R University :
            1. Menyelenggarakan pendidikan akademik yang berkualitas;
            2. Mewujudkan pendidikan tinggi yang bermutu untuk mendukung daya saing bangsa;
            3. Meningkatkan pembinaan keterampilan teknis, karakter, dan prestasi mahasiswa.
       ''')

#memasukkan informasi
informasi_list = []
def informasi():
    while True:
        judul = input(" \nJudul Informasi  : ")
        detail = input ("Detail           : ")
        informasi_list.append([judul, detail])
        lanjut = input("\nApakah Anda ingin menambah informasi lagi? (y/n): ").strip().lower()
        print("Informasi Berhasil Disimpan")
        if lanjut != 'y':
            break
        print()  

#memasukkan data mahasiswa
def menyimpan(nama, nim, ttl, jenis_kelamin, agama, alamat, warga_negara, jurusan, email):
    with open('data_mahasiswa.txt', 'a') as file:
        file.write (f"{nama}, {nim}, {ttl}, {jenis_kelamin}, {agama}, {alamat}, {warga_negara}, {jurusan}, {email}\n")
    print ('\nData Berhasil Disimpan\n')

#menampilkan data mahasiswa
def tampilkan():
    with open('data_mahasiswa.txt', 'r') as file:
        baris = file.readlines()
        if not baris:
                os.system('cls')
                print("\nData Mahasiswa tidak Tersedia\n")
        else:
            for line in baris:
                print('\nData Mahasiswa : ')
                data = line.strip().split(', ')
                if len(data) == 9:  
                    data_mahasiswa = {
                        'Nama'                      : data[0],
                        'NIM'                       : data[1],
                        'Tempat/Tanggal Lahir'      : data[2],
                        'Jenis Kelamin'             : data[3],
                        'Agama'                     : data[4],
                        'Alamat'                    : data[5],
                        'Warga Negara'              : data[6],
                        'Jurusan'                   : data[7],
                        'Email'                     : data[8]
                    }
                    for key, value in data_mahasiswa.items():
                        print(f"{key:<25}: {value:<25}")
                    print()
                else:
                    print("\nData tidak lengkap atau Ada Kesalahan.")

#memasukkan absensi 
absensi = []  

def tambahkan_kehadiran(absensi):
    tanggal = input("\nMasukkan Hari/Tanggal Perkuliahan : ")
    waktu_mulai = input("Masukkan Waktu Mulai              : ")
    waktu_selesai = input("Masukkan Waktu Selesai            : ")
    deskripsi = input("Masukkan Mata Kuliah Kegiatan     : ")
    dosen = input ("Masukkan Nama Dosen Pengajar      : ")
    tempat = input ("Masukkan Tempat Perkuliahan       : ")
    status_absen = input ("Masukkan Status Absen             : ")
    absensi.append([tanggal, waktu_mulai, waktu_selesai, deskripsi, dosen, tempat, status_absen])
    print('Kehadiran Berhasil Ditambahkan.\n')

def tampilkan_kehadiran(absensi):
    if len(absensi) == 0:
        print('\nKehadiran Belum Ada')
    else:
        print ('\nBerikut Daftar Kehadiran selama Perkulihan')
        print('| {:^4} | {:^17} | {:^11} | {:^12} | {:^18} | {:^21} | {:^24} | {:^12} |'.format('No.','Hari/Tanggal','Waktu Mulai','Waktu Selesai','Mata Kuliah', 'Dosen', 'Tempat', 'Status Absen' ))
        print('-' * 140)
        for i in range(len(absensi)):
            print('| {:^4} | {:^17} | {:^11} | {:^12} | {:^18} | {:^21} | {:^24} | {:^12} |'.format(i+1, absensi[i][0], absensi[i][1], absensi[i][2], absensi[i][3], absensi[i][4], absensi[i][5], absensi[i][6]))

#memasukkan hasil studi
def hasil_studi ():
    mata_kuliah = [
            "Kalkulus II",
            "Geometri Analitik",
            "Aljabar Linier Elementer",
            "Algoritma dan Pemograman",
            "Matematika Diskrit",
            "Kewarganegaraan",
            "Pancasila"
        ]

    nilai_mahasiswa = []
    for i in mata_kuliah:
        print(f"\nMasukkan nilai untuk {i}:")
        uts = int(input("Nilai UTS   : "))
        uas = int(input("Nilai UAS   : "))
        tugas = int (input("Nilai Tugas : "))
        rata_rata = (uts + uas + tugas)/3
        print ("Rata-Rata   : ", rata_rata)
        print (''' \nKeterangan :
                Rata-Rata    >=  90 : A
                80 < Rata-Rata < 90 : B
                70 < Rata-Rata <=80 : C
                60 < Rata-Rata <=70 : D
                Rata-Rata    <=  60 : E
               ''')
        predikat = input ("Predikat    : ")
        nilai_mahasiswa.append([uts, uas, tugas, predikat])
    return nilai_mahasiswa

#menampilkan hasil studi
def tampilkan_hasil_studi(nilai_mahasiswa):
    if len(nilai_mahasiswa) == 0:
        os.system('cls')
        print ("\nNilai Mahasiswa Belum Tersedia\n")
    else:
        from tabulate import tabulate
        header = ["Mata Kuliah", "Nilai UTS", "Nilai UAS", "Nilai Tugas", "Predikat"]
        print(tabulate(nilai_mahasiswa, headers=header, tablefmt="grid"))

nilai_mahasiswa = []
status= ''

while True :
    print ("\nMENU")
    menu = ("1. Masukkan Informasi")
    print (menu)
    menu = ("2. Masukkan Data Mahasiswa")
    print(menu)
    menu = ("3. Masukkan Status Mahasiswa")
    print(menu)
    menu = ("4. Masukkan Hasil Studi")
    print(menu)
    menu = ("5. Informasi")
    print(menu)
    menu = ("6. Data Mahasiswa")
    print(menu)
    menu = ("7. Status Mahasiswa")
    print(menu)
    menu = ("8. Absensi")
    print(menu)
    menu = ("9. Hasil Studi")
    print(menu)
    menu = ("10. Log Out")
    print(menu)

    menu = (input("Pilih Menu : "))

    if menu == "1" :
        informasi()
        time.sleep(2)
        os.system('cls')

    elif menu == "2":
        nama = input ("\nNama                 : ") 
        nim = int(input ("NIM                  : ")) 
        ttl =  input ("Tempat/Tanggal Lahir : ")
        jenis_kelamin = input ("Jenis Kelamin        : ")
        agama = input ("Agama                : ")
        alamat = input ("Alamat               : ")
        warga_negara = input ("Warga Negara         : ")
        jurusan = input ("Jurusan              : ")
        email = input ("Email                : ")
        menyimpan(nama, nim, ttl, jenis_kelamin, agama, alamat, warga_negara, jurusan, email)
        time.sleep(2)
        os.system('cls')

    elif menu == "3":
        status= input ("\nStatus Mahasiswa (Aktif/Berhenti Sementara/ Tidak Aktif) : ").strip().lower()
        time.sleep(2)
        os.system('cls')

    elif menu == "4":
       nilai_mahasiswa = hasil_studi()
       time.sleep(2)
       os.system('cls')

    elif menu == "5":
        if len(informasi_list) == 0:
            os.system('cls')
            print("\nTidak Ada Informasi yang Tersedia\n")
        else: 
            for i, info in enumerate(informasi_list , 1):
                print(f"\n\tInformasi {i}:")
                print(f"  Judul : {info[0]}")
                print(f"  Detail: {info[1]}")
        
    elif menu == "6":
        os.system('cls')
        tampilkan()

    elif menu == "7":
        os.system('cls')
        if not status :
            print ("\nStatus Mahasiswa Belum Tersedia\n")
        else:
            print("\nStatus Mahasiswa : ", status)
        

    elif menu == "8":
        os.system('cls')
        tambahkan_kehadiran(absensi)
        tampilkan_kehadiran(absensi)

    elif menu == "9":
        tampilkan_hasil_studi(nilai_mahasiswa)
        input("\nTekan Enter untuk Melanjutkan...\n")

    elif menu == "10":
        print(" "*30, end='')
        print(":"*45)
        tutup = "        Terima Kasih Telah Berkunjung        "
        print(" "*30, end='')
        cprint(tutup, "white", "on_light_blue")
        print(" "*30, end='')
        print(":"*45)
        print ("No BP : 2310432022 and 2310432018")
        print ("No BP   : 2310432022 and 2310432018\n")
        break
    
    else:
        cprint ("Menu yang Dipilih Tidak Valid. Silahkan Coba Lagi!", "black", "on_light_green")
        time.sleep(2)
        os.system('cls')
