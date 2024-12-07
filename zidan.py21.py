# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 13:25:15 2024

@author: ASUS
"""

class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.__nilai = nilai

    @property
    def detail(self):
        return f"Nama: {self.nama}\nNilai: {self.__nilai}"

    @property
    def nilai(self):
        return self.__nilai

    @nilai.setter
    def nilai(self, nilai_baru):
        if isinstance(nilai_baru, int):
            self.__nilai = nilai_baru
        else:
            print("Nilai harus berupa angka!")

def input_data(mahasiswa):
    nama = input("Masukkan Namamu: ")
    nilai = int(input("Masukkan Nilaimu: "))
    mahasiswa.nama = nama
    mahasiswa.nilai = nilai

def tampilkan_data(mahasiswa):
    print(mahasiswa.detail)

def ubah_data(mahasiswa):
    op = input("Apa yang ingin diubah (Nama/Nilai): ")
    if op.lower() == "nama":
        nama_baru = input("Masukkan Nama baru: ")
        mahasiswa.nama = nama_baru
    elif op.lower() == "nilai":
        nilai_baru = int(input("Masukkan Nilai baru: "))
        mahasiswa.nilai = nilai_baru
    else:
        print("Masukkan opsi yang sesuai antara Nama/Nilai!")

def main():
    mahasiswa = Mahasiswa(None, None)
    while True:
        print("===== Program OOP =====")
        print("1. Mendeklarasikan Objek")
        print("2. Menampilkan Objek")
        print("3. Merubah Nilai Objek")
        print("4. Keluar Dari Program")
        pilihan = int(input("Masukkan Pilihan Berupa Angka (1/2/3/4): "))

        if pilihan == 1:
            input_data(mahasiswa)
        elif pilihan == 2:
            tampilkan_data(mahasiswa)
        elif pilihan == 3:
            ubah_data(mahasiswa)
        elif pilihan == 4:
            print("Terima Kasih Sudah Menggunakan Program Saya")
            break
        else:
            print("Invalid Input!")

if __name__ == "__main__":
    main()
    
    