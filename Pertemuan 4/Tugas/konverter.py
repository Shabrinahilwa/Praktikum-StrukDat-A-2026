import kurs

#IDR ke mata uang lain
def konversi_dari_IDR(jumlah, mata_uang):
    nilai_mata_uang = kurs.kurs_uang[mata_uang]
    hasil = jumlah / nilai_mata_uang
    return hasil

# Mata uang lain ke IDR
def konversi_ke_IDR(jumlah, mata_uang):
    nilai_mata_uang = kurs.kurs_uang[mata_uang]
    hasil = jumlah * nilai_mata_uang
    return hasil
