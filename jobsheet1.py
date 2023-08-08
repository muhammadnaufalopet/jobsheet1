import random
from guess import cek

jawaban = random.randint(1, 2)

tebakan = int(input('tebak angka dari 1 sampai 2: '))

if cek(tebakan, jawaban):
    print("jawaban kamu benar!")
else:
     print("jawaban kamu salah!")
    