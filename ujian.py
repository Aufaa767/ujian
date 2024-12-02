daftar_hewan = ["kucing", "beruang", "jerapah", "harimau", "kicau"]

def insert_cos():
    print("Daftar hewan saat ini:", daftar_hewan)
    num_inserts = int(input("Berapa banyak hewan yang ingin dimasukan ke daftar? "))
    
    for i in range(num_inserts):
        position = int(input(f"Masukkan posisi hewan yang ingin dimasukan ke daftar {i + 1}: "))
        input_ins = input(f"Masukkan nama hewan {i + 1} yang ingin dimasukan ke daftar: ")
        daftar_hewan.insert(position, input_ins)
        print(f'Hewan yang dimasukan ke daftar: {input_ins} di posisi {position}')
    
    print("Daftar hewan setelah beberapa penyesuaian:", daftar_hewan)


def pop_cos():
    print("Daftar hewan saat ini:", daftar_hewan)
    if daftar_hewan:
        index = int(input("Masukkan indeks hewan yang ingin dihapus: "))
        if 0 <= index < len(daftar_hewan):
            popped = daftar_hewan.pop(index)
            print(f'hewan yang dihapus: {popped}')
            print("Daftar hewan setelah pop:", daftar_hewan)
        else:
            print("Indeks tidak valid. Silakan masukkan indeks yang benar.")
    else:
        print("Daftar kosong, tidak ada yang dapat dihapus.")

def index_cos():
    print("Daftar hewan saat ini:", daftar_hewan)
    input_idx = input("Masukkan nama hewan untuk mencari indeksnya: ")
    if input_idx in daftar_hewan:
        idx = daftar_hewan.index(input_idx)
        print(f'Indeks dari hewan {input_idx}: {idx}')
    else:
        print(f"hewan {input_idx} tidak ditemukan di daftar.")

def count_cos():
    print("Daftar hewan saat ini:", daftar_hewan)
    input_cnt = input("Masukkan nama hewan untuk menghitung jumlah kemunculannya: ")
    cnt = daftar_hewan.count(input_cnt)
    print(f'hewan {input_cnt} muncul sebanyak {cnt} kali di daftar.')

def main():
    nama = "Aufa Maulana Hakim"
    kelas = "1IA16"
    NPM = "50424205"
    print("Hallo, saya admin", nama,"dari kelas", kelas,"NPM", NPM)
    x = True
    while x:
        print("""
=========================================================
Selamat Datang di Sistem Pendaftaran Hewan Kebun Binatang 
1.Tambahkan Hewan Baru
2.Cek Daftar Hewan
3.Hapus Hewan
4.Hitung Hewan
5.Exit
=========================================================
        """)
        input_user = input("Masukkan pilihan menu (1-5): ")
        if input_user == '1':
            insert_cos()
        elif input_user == '2':
            index_cos()
        elif input_user == '3':
            pop_cos()
        elif input_user == '4':
            count_cos()
        elif input_user == '5':
            print("Keluar dari program.")
            break
        else:
            print("Input tidak valid. Silakan pilih menu dari 1 hingga 8.")

if __name__ == "__main__":
    main()

    
    
    
    