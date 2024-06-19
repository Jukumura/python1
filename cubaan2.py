import time

def welcome_message():
    print("--------------------------------------------------")
    print("Selamat Datang ke Permainan Teka Teki !")
    print("--------------------------------------------------")
    time.sleep(1)

def display_instructions(chances):
    print(f"Anda harus pilih jawapan yang tepat.\nAnda akan dapat 1 mata bagi jawapan yang betul.\n")
    time.sleep(2)

def ask_question(question, options, correct_answer, chances):
    print("==================================================")
    print(question)
    for option in options:
        print(option)
    print("\n")

    for i in range(chances):
        answer = input("Jawapan: ").lower()
        if answer == correct_answer:
            print("Tahniah! Anda Betul!\n")
            return 1
        else:
            print("Salah!\n")
            time.sleep(0.5)
            print(f"Jawapannya ialah {correct_answer.upper()}\n\n")
            return 0

def main():
    welcome_message()
    
    chances = 1
    display_instructions(chances)
    
    score = 0
    questions = [
        {
            "question": "1) Antara banyak-banyak binatang, yang manakah boleh terbang?",
            "options": ["(A) Unta", "(B) Kuda", "(C) Itik Nila", "(D) Zirafah"],
            "answer": "c"
        },
        {
            "question": "2) Singa apa warna merah dan putih?",
            "options": ["(A) Singa Laut", "(B) Singa Afrika", "(C) Singa Betina", "(D) Singapura"],
            "answer": "d"
        },
        {
            "question": "3) Kelawar apa tak boleh terbang?",
            "options": ["(A) Kelawar Mati", "(B) Batman", "(C) Kelawar Buta", "(D) Kelawar Jantan"],
            "answer": "a"
        }
    ]
    
    for question in questions:
        score += ask_question(question["question"], question["options"], question["answer"], chances)
        time.sleep(2)
    
    # Calculate percentage
    percentage = (score / len(questions)) * 100
    
    # Display final score and percentage
    print("==================================================")
    print(f"Jawapan yang betul: {score}")
    print(f"Peratusan markah anda: {percentage:.2f}%")

if __name__ == "__main__":
    main()
