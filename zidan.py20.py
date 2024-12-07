# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 13:14:35 2024

@author: ASUS
"""

class Biodata:
    jumlah_siswa = 0

    def __init__(self, nama, nim, tahun):
        self.nama = nama
        self.nim = nim
        self.tahun = tahun
        Biodata.jumlah_siswa += 1

    def print_biodata(self):
        print(f"Nama: {self.nama}\nNIM: {self.nim}\nAngkatan: {self.tahun}")

    def ubah_nama(self, nama_baru):
        self.nama = nama_baru

    @classmethod
    def tampilkan_semua_siswa(cls):
        print(f"Jumlah siswa: {cls.jumlah_siswa}")

nama = input("Masukkan Namamu: ")
nim = input("Masukkan NIM kamu: ")
tahun = int(input("Masukkan tahun Angkatanmu: "))

siswa1 = Biodata(nama, nim, tahun)
siswa1.print_biodata()
Biodata.tampilkan_semua_siswa()