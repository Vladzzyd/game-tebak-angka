import random
#WARNA DIPAKAI
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

jawaban = None
batas_bawah = 0
batas_atas = 100
total_tebakan = 0

def border():
    return CYAN + "="*40 + RESET

def kotak(teks, panjang=40):
    teks = teks.center(panjang-6)
    return CYAN + "|| " + RESET + teks + CYAN + " ||" + RESET

def input_angka(angka):
    while True:
        try:
            return int(input(angka))
        except ValueError:
            print(RED + "jawaban harus berupa angka!" + RESET)

def jawabannya():
    global jawaban
    jawaban = random.randint(0,100)

def ditebak(tebakan):
    global jawaban, batas_bawah, batas_atas, total_tebakan
    total_tebakan += 1
    
    if not jawaban:
        jawabannya()

    if jawaban == tebakan:
        print(GREEN + "jawabanmu benar!!" + RESET)
        print(GREEN + f"total tebakan: {total_tebakan}" + RESET)

        jawaban = None
        batas_bawah = 0
        batas_atas = 100
        total_tebakan = 0

        return "y"

    else:
        if tebakan < jawaban:
            print(YELLOW + "⬆️ jawabanmu terlalu rendah!!" + RESET)
            batas_bawah = tebakan
            return None
        elif tebakan > jawaban:
            print(YELLOW + "⬇️ jawabanmu terlalu tinggi!!" + RESET)
            batas_atas = tebakan
            return None

while True:
    print(border())
    print(kotak("GAME TEBAK ANGKA"))
    while True:
        print(border())
        print(kotak(f"Tebak angka antara {batas_bawah} - {batas_atas}"))
        print(border())

        tebakan = input_angka("masukkan tebakan mu: ")

        if not (batas_bawah < tebakan < batas_atas):
            print(RED + f"masukkan angka diantara {batas_bawah} - {batas_atas}" + RESET)
            continue        
        
        hasil = ditebak(tebakan)
        if hasil == "y":
            break

    while True:
        ulang = input("ingin bermain lagi? (y/n): ").strip().lower()
        if ulang in ("y","n"):
            break
    
    if ulang == "n":
        print(CYAN + "termakasih sudah bermain!!" + RESET)
        break