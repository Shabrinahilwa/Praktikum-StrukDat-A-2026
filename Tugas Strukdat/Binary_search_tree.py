class Node: 
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    #Fungi menambahkan node root
    def insert_root(self, data):
        self.root = Node(data)
    
    #Fungsi menambahkan node sebelah kiri
    def insert_left(self, parent_node, data):
        if parent_node is None:
            parent_node = Node(data)
        else:
            new_node= Node(data)
            new_node.left = parent_node.left
        parent_node.left = new_node
    
    #Fungsi menambahkan node sebelah kanan
    def insert_right(self, parent_node, data):
        if parent_node is None:
            parent_node = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
        parent_node.right = new_node
    
    #Menambahkan buku baru ke dalam BST sesuai aturan ID
    def insert(self, id_buku, judul):
        new = Node(id_buku, judul)

        if self.root is None:
            self.root = new
            print(f"[INSERT] Berhasil Memasukkan: ID {id_buku} - {judul}")
            return

        Q = self.root
        P = self.root

        while Q is not None and new.id_buku != P.id_buku:
            P = Q   
            if new.id_buku < P.id_buku:
                Q = P.left
            else:
                Q = P.right
        
        if new.id_buku == P.id_buku:
            print("Data duplikat")
            return
            
        if new.id_buku < P.id_buku:
            #Jika iya
            P.left = new
        else: 
            #Jika tidak 
            P.right = new

        print(f"[INSERT] Berhasil Memasukkan: ID {id_buku} - {judul}")

    #Mencari apakah suatu buku ada di katalog berdasarkan ID-nya.
    def search(self, id_buku):
        current = self.root
        while current is not None:
            if id_buku == current.id_buku:
                print(f"[SEARCH] Buku ditemukan: ID {current.id_buku} - {current.judul}")
                return current
            elif id_buku < current.id_buku:
                current = current.left
            else:
                current = current.right
        return None
    
    #Menampilkan semua koleksi buku secara urut dari ID terkecil ke terbesar.
    def traversal_inorder(self, node):
        if node is not None:
            self.traversal_inorder(node.left)
            print(f"ID {node.id_buku} - {node.judul}")
            self.traversal_inorder(node.right)

    #Menemukan buku dengan ID terkecil 
    def get_min(self):
        if self.root is None:
            return None
            
        min_node = self.root
        while min_node.left is not None:
            min_node = min_node.left
        return min_node
    
    #Menemukan buku dengan ID terbesar
    def get_max(self):
        if self.root is None:
                return None
            
        max_node = self.root
        while max_node.right is not None:
            max_node = max_node.right
        return max_node
    
    #Menghitung total ketinggian (height) dari tree yang terbentuk.
    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height +1
        
data_buku = BinarySearchTree()

print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
print("=======================================================")

#Masukkan buku-buku:
data_buku.insert(50, "Dasar Pemograman")
data_buku.insert(30, "Struktur Data")
data_buku.insert(70, "Kecerdasan Buatan")
data_buku.insert(20, "Matematika Diskrit")
data_buku.insert(40, "Basis Data")
data_buku.insert(60, "Jaringan Komputer")
data_buku.insert(80, "Sistem Operasi")

#Melihat apakah buku sudah terurut otomatis.
print("\n[INFO] Koleksi Buku (In-Order Traversal):")
data_buku.traversal_inorder(data_buku.root)

#Cari buku dengan ID 60 .
print("\n[SEARCH] mencari id 60...", end=" ")
buku_1= data_buku.search(60)
if buku_1 is not None:
    print(f"Ditemuan! Judul: ", buku_1.judul )
else: 
    print(f"Data tidak ditemukan.")

#Cari buku dengan ID 100
print("[SEARCH] mencari id 100...", end=" ")
buku_2= data_buku.search(100)
if buku_2 is not None:
    print(f"Ditemuan! Judul: ", buku_2.judul )
else: 
    print(f"Data tidak ditemukan.")

#Tampilkan ID buku terkecil dan terbesar dalam katalog.
min_node = data_buku.get_min()
print(f"\n[STATISTIK] ID TERKECIL: {min_node.id_buku} - {min_node.judul}")
max_node = data_buku.get_max()
print(f"[STATISTIK] ID TERBESAR: {max_node.id_buku} - {max_node.judul}")

#Tampilkan berapa Height dari tree yang terbentuk.
height = data_buku.height(data_buku.root)
print(f"[INFO] Tinggi (Height) Tree: {height}")
print("=========================================")
print("Simulasi selesai!")