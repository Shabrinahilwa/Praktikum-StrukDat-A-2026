
class Node: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Insert manual ke dalam Binary Tree
class BinaryTree:
    def __init__(self):
        self.root = None
     
    #Menambahkan Root
    def insert_root(self, data):
        self.root = Node(data)
    
    #Menambahkan Node sebelah kiri
    def insert_left(self, parent_node, data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node
    
    #Menambahkan Node sebelah kanan
    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node

tree = BinaryTree()  

tree.insert_root("A") 
tree.insert_left(tree.root, "B")
tree.insert_left(tree.root.left, "D")
tree.insert_right(tree.root.left, "E")
tree.insert_right(tree.root, "C")
tree.insert_right(tree.root.right, "F")

#Audit Prioritas: Mengecek gudang utama sebelum cabang-cabangnya.
def traverse_preorder(node):
    if node is not None:
        print(node.data, end=" - ")
        traverse_preorder(node.left)
        traverse_preorder(node.right)

#Audit Berurutan: Mengecek dari jalur kiri, lalu pusat, baru ke kanan.
def traverse_inorder(node):
    if node is not None:
        traverse_inorder(node.left)
        print(node.data, end=" - ")
        traverse_inorder(node.right)

#Audit Akhir: Mengecek semua cabang terlebih dahulu sebelum kembali kegudang pusat.
def traverse_postorder(node):
    if node is not None:
        traverse_postorder(node.left)
        traverse_postorder(node.right)
        print(node.data, end=" - ")

#Menampilkan daftar gudang (Leaf Node)
def get_leaf_nodes(node):
    if node is None:
        return []
    if node.left is None and node.right is None:
        return [node.data]
    
    return get_leaf_nodes(node.left) + get_leaf_nodes(node.right)

print("SISTEM AUDIT DISTRIBUSI 'CEPAT SAMPAI'")
print("======================================")
print("[INFO] Membangun Struktur Gudang...")
print("[INFO] Struktur berhasil dibuat.")

#Memanpilkan hasil penelurusan Pre-Order, In-Order, dan Post-Order
print("\nHASIL AUDIT:")
print("1. Pre-Order  : ", end=" ")
traverse_preorder(tree.root)
print("\n2. In-Order   : ", end=" ")
traverse_inorder(tree.root)
print("\n3. Post-Order : ", end=" ")
traverse_postorder(tree.root)

#Menampilkan daftar semua Leaf Nodes
print("\n")
print(f"[DATA] Gudang Ujung (Leaf Nodes): {(get_leaf_nodes(tree.root))}")
print("======================================")
print("Audit Selesai!")