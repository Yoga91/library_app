class Buku:
    def __init__(self, judul, penulis, total_halaman):
        self.judul = judul
        self.penulis = penulis
        self.total_halaman = total_halaman
        self.halaman_awal = 1

    def __str__(self):
        return f"{self.judul} ditulis oleh {self.penulis} ({self.total_halaman} halaman)"
    
    
class Perpustakaan:
    def __init__(self):
        self.buku_perpus = []
    
    def tambah_buku(self, Buku):
        self.buku_perpus.append(Buku)

    def hapus_buku(self, Buku):
        self.hapus_buku.remove(Buku)

    def tampilkan_buku(self):
        print("\nBuku di Perpustakaan :\n")
        for Buku in self.buku_perpus:
            print(f"- {Buku}\n")

class User:
    def __init__(self, username):
        self.username = username
        self.buku_perpus = Perpustakaan()
        self.buku_dibaca = None

    def tambah_buku_perpustakaan(self, Buku):
        self.buku_perpus.tambah_buku(Buku)
    
    def hapus_buku_perpustakaan(self, Buku):
        self.buku_perpus.hapus_buku(Buku)


    def daftar_buku_dibaca(self, Buku):
        self.buku_dibaca = Buku

    def next_halaman(self):
        if self.buku_dibaca:
            if self.buku_dibaca.halaman_awal < self.buku_dibaca.total_halaman:
                self.buku_dibaca.halaman_awal += 1
                print(f"\n{self.username} membaca halaman {self.buku_dibaca.halaman_awal} dari buku {self.buku_dibaca.judul}\n")
            else:
                print(f"{self.username} telah selesai membaca {self.buku_dibaca.judul}\n")
        else:
            print("Tidak ada buku yang dibaca")

    def tampilkan_buku_perpus(self):
        self.buku_perpus.tampilkan_buku()


if __name__ == "__main__":
    
    buku1 = Buku("Wiro Sableng", "Eep Surecep", 120)
    buku2 = Buku("Detektif Conan", "Hondawati Mugiwara", 200)
    buku3 = Buku("Joko Tingkir", "Otong Surotong", 250)
    buku4 = Buku("Rayuan Wanita Gila", "Nadin Amizah", 50)
    buku5 = Buku("Si Manis Jembatan Merah", "John Joko", 20)
    buku6 = Buku("Mandi di Pagi hari", "Michael Ucup", 55)

    username1 = User("Timo")
    username2 = User("Faqih")
    username3 = User("Ucyup")
    username4 = User("Miko")

    username1.tambah_buku_perpustakaan(buku1)
    username1.tambah_buku_perpustakaan(buku2)
    username2.tambah_buku_perpustakaan(buku3)
    username3.tambah_buku_perpustakaan(buku4)
    username3.tambah_buku_perpustakaan(buku5)
    username4.tambah_buku_perpustakaan(buku6)
    
    username1.tampilkan_buku_perpus()
    username2.tampilkan_buku_perpus()
    username3.tampilkan_buku_perpus()
    username4.tampilkan_buku_perpus()

    username1.daftar_buku_dibaca(buku1)
    username3.daftar_buku_dibaca(buku2)

    username1.next_halaman()
    username3.next_halaman()

    username1.daftar_buku_dibaca(buku1)
    username3.daftar_buku_dibaca(buku2)

    username1.next_halaman()
    username3.next_halaman()



