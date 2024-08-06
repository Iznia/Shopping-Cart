'''
============================================================
Graded Challenge 1

Nama  : Iznia Azyati
Batch : RMT -032

Program ini dibuat untuk aplikasi belanja Toko Iznia

Program ini menggunakan konsep Conditionals, Loops, 
Functions, Object-Oriented Programming, Python Unit Test, 
dan Computational Thinking
============================================================
'''

class CartItem:
    ''' Fungsi ini bertujuan untuk merepresentasikan sebuah item atau barang dalam keranjang belanja.
    '''
    def __init__(self, nama, harga):
        '''Fungsi ini bertujuan untuk membuat Cart Item dan membutuhkan input berupa nama barang dan harga barang.
        
        Contoh: 
        CartItem('kemeja',55_000)
        ------
        '''
        self.nama = nama
        self.harga = harga


class ShoppingCart:
    '''
    Kelas Shopping Cart ini merepresentasikan keranjang belanja.
        
    Kelas ini bertujuan untuk mengelola barang-barang di dalam keranjang dan menyediakan metode 
    untuk menambah, menghapus, menampilkan, dan menghitung total belanja
    '''
    def __init__(self):
        self.items = []
    
    # Untuk menambahkan kelas 'CartItem' ke dalam keranjang
    def add_item(self, nama, harga):
        self.items.append(CartItem(nama, harga))
        print(f'Barang "{nama}" berhasil dimasukkan ke keranjang.')


    # Untuk menghapus kelas 'CartItem' ke dalam keranjang
    def remove_item(self, nama):

        print("=========================")
        print("Barang Terhapus")
        print("=========================")

        # Menggunakan for loop untuk menghapus barang dari keranjang belanja.
        for item in self.items:
            if item.nama == nama:
                self.items.remove(item)
                print(f'"{nama}" berhasil dihapus dari keranjang belanja.')
                return
        print(f'Barang "{nama}" tidak ditemukan di keranjang.')
    

    # Untuk menampilkan semua barang yang ada dalam keranjang.
    def display_items(self):

        print("=========================")
        print("Data Barang di Keranjang")
        print("=========================")

        # Mengecek tidak barang dalam keranjang belanja
        if not self.items:
            print("Keranjang belanja kosong.")
        
        # Jika ada barang maka tampilkan nama dan harga barang
        else:
            print("Barang di Keranjang: ")
            for idx, item in enumerate(self.items):
                print(f"{idx}. {item.nama} - Rp {item.harga:.2f}")
    
    # Menghitung total semua barang yang ada dalam keranjang
    def total_price(self):
        return sum(item.harga for item in self.items)
    

    print("----------------------------------------------------")
    print("Selamat Datang di Toko Retail Iznia!")
    print("----------------------------------------------------")

    # Untuk menjalankan jika user/pengguna melakukan interaksi dengan keranjang belanja
    def run(self):
        while True: 
            print('''
            ===================================================
            Pilihan Menu di Keranjang Belanja Toko Iznia
            ===================================================
            
            Menu: 
                1. Tambah Barang
                2. Hapus Barang
                3. Tampilkan Barang di Keranjang
                4. Lihat Total Belanja
                5. Exit
                  
            ''')

            choice = input("Pilihan:")
            if choice == '1':
                nama = input("Masukkan nama barang: ")
                harga = float(input("Masukkan harga: "))
                self.add_item(nama, harga)

            elif choice == '2':
                nama = input("Masukkan nama barang yang ingin dihapus: ")
                self.remove_item(nama)
            
            elif choice == '3':
                self.display_items()
            
            elif choice == '4':
                total = self.total_price()
                print(f"Total Belanja: Rp {total:2f}") 
            
            elif choice == '5':
                print("-----------------------------------------------------------")
                print("Barang belanja tersimpan, silahkan ke kasir")
                print("Sampai Jumpa!! Terima kasih sudah belanja di Toko Iznia :)")
                print("-----------------------------------------------------------")
                break

            else:
                print("Pilihan salah. Coba lagi yaa :)")
            
# Idiom untuk membuat objek 'ShoppingCart' dan menjalankan metode 'run'
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.run()

