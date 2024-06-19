import time
print("--------------------------------------------------")
#Welcome the user
print("Selamat Datang ke Permainan Teka Teki !")
time.sleep(1)
print("--------------------------------------------------")

#Chances
chances=1
print("Anda harus pilih jawapan ", chances,"yang tepat.\nAnda akan dapat 1 mata bagi jawapan yang betul.\n")
time.sleep(2)

#score
score=0

#question 1
print("==================================================")
question_1=print("1) Antara banyak-banyak binatang, yang manakah boleh terbang?\n(A) Unta\n(B) Kuda\n(C) Itik Nila\n(D) Zirafah\n\n")
answer_1= "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("Tahniah! Anda Betul!\n")
        score = score + 1
        break
    else:
        print("Salah!\n")
        time.sleep(0.5)
        print("Jawapannya ialah", answer_1, "\n\n")

time.sleep(2)

#question 2
print("==================================================")
question_2 = print("2)Singa apa warna merah dan putih?\n(A) Singa Laut\n(B) Singa Afrika\n(C) Singa Betina\n(D) Singapura\n\n")  
answer_2 = "d"

for i in range(chances):
    answer = input("answer: ")
    if (answer.lower() == answer_2):
        print("Tahniah! Anda betul!\n")
        score = score + 1
        break
    else:
        print("Salah!\n ")
        time.sleep(0.5)
        print("Jawapannya ialah", answer_2, "\n\n")

time.sleep(2)

#question 3
print("==================================================")
question_3 = print("2)Kelawar apa tak boleh terbang?\n(A) Kelawar Mati\n(B) Batman\n(C) Kelawar Buta\n(D) Kelawar Jantan\n\n")  
answer_3 = "a"

for i in range(chances):
    answer = input("answer: ")
    if (answer.lower() == answer_3):
        print("Tahniah! Anda betul!\n")
        score = score + 1
        break
    else:
        print("Salah!\n ")
        time.sleep(0.5)
        print("Jawapannya ialah", answer_3, "\n\n")

time.sleep(2)

# Calculate percentage
percentage = (score / 3) * 100

# Display final score and percentage
print("==================================================")
print(f"Jawapan yang betul: {score}")
print(f"Peratusan markah anda: {percentage:.2f}%")


