import random
import time

knowledge_base = {
    "siapa kamu?": ["Saya adalah chatbot.", "Saya hanyalah sebuah chatbot sederhana."],
    "siapa kamu": ["Saya adalah chatbot.", "Saya hanyalah sebuah chatbot sederhana."],
    "siapa namamu?": ["Nama saya adalah ChatBot.", "Anda bisa memanggil saya ChatBot."],
    "siapa namamu": ["Nama saya adalah ChatBot.", "Anda bisa memanggil saya ChatBot."],
    "bagaimana kabarmu?": ["Saya hanya sebuah program, jadi saya tidak punya perasaan, tapi terima kasih sudah bertanya:)"],
    "bagaimana kabarmu": ["Saya hanya sebuah program, jadi saya tidak punya perasaan, tapi terima kasih sudah bertanya:)"],
    "apa yang bisa kamu lakukan?": ["Saya bisa merespons pertanyaan-pertanyaan sederhana dan berbincang-bincang dasar."],
    "apa yang bisa kamu lakukan": ["Saya bisa merespons pertanyaan-pertanyaan sederhana dan berbincang-bincang dasar."],
    "apa ibukota Perancis?": ["Ibukota Perancis adalah Paris."],
    "apa ibukota Perancis": ["Ibukota Perancis adalah Paris."],
    "apa akar kuadrat dari 16?": ["Akar kuadrat dari 16 adalah 4."],
    "apa akar kuadrat dari 16": ["Akar kuadrat dari 16 adalah 4."],
    "bagaimana cuacanya hari ini?": ["Maaf, saya tidak dapat memberikan informasi cuaca real-time."],
    "bagaimana cuacanya hari ini": ["Maaf, saya tidak dapat memberikan informasi cuaca real-time."],
    "apa itu Python?": ["Python adalah bahasa pemrograman tingkat tinggi yang diinterpretasikan."],
    "apa itu Python": ["Python adalah bahasa pemrograman tingkat tinggi yang diinterpretasikan."],
    "berapa populasi Jepang?": ["Sampai tahun 2021, populasi Jepang sekitar 126 juta jiwa."],
    "berapa populasi Jepang": ["Sampai tahun 2021, populasi Jepang sekitar 126 juta jiwa."],
    "apa saja warna pelangi?": ["Warna-warna pelangi adalah merah, jingga, kuning, hijau, biru, nila, dan ungu."],
    "apa saja warna pelangi": ["Warna-warna pelangi adalah merah, jingga, kuning, hijau, biru, nila, dan ungu."],
    "apa makna dari hidup?": ["Makna hidup adalah pertanyaan filosofis yang bervariasi tergantung pada keyakinan dan perspektif pribadi."],
    "apa makna dari hidup": ["Makna hidup adalah pertanyaan filosofis yang bervariasi tergantung pada keyakinan dan perspektif pribadi."],
    "apa jarak antara Bumi dan Bulan?": ["Rata-rata jarak antara Bumi dan Bulan adalah sekitar 384.400 kilometer (238.900 mil)."],
    "apa jarak antara Bumi dan Bulan": ["Rata-rata jarak antara Bumi dan Bulan adalah sekitar 384.400 kilometer (238.900 mil)."],
    "planet terbesar di tata surya kita adalah apa?": ["Planet terbesar di tata surya kita adalah Jupiter."],
    "planet terbesar di tata surya kita adalah apa": ["Planet terbesar di tata surya kita adalah Jupiter."],
    "berapa titik didih air?": ["Titik didih air adalah 100 derajat Celsius (212 derajat Fahrenheit) pada permukaan laut."],
    "berapa titik didih air": ["Titik didih air adalah 100 derajat Celsius (212 derajat Fahrenheit) pada permukaan laut."],
}
fallback_response = ["Maaf, saya tidak mengerti itu.", "Saya tidak yakin bagaimana merespons itu."]
greetings = ["hai", "halo", "hey", "selamat pagi", "selamat siang", "selamat malam"]
farewells = ["selamat tinggal", "sampai jumpa", "goodbye", "bye", "bye-bye"]

def respond_to_greeting():
    time.sleep(1)
    return random.choice(greetings)

def respond_to_farewell():
    time.sleep(1)
    return random.choice(farewells)

def respond_to_question(question):
    time.sleep(1)
    response = knowledge_base.get(question.lower(), fallback_response)
    return random.choice(response)

def teach_new_response(question, response):
    if question.lower() in knowledge_base:
        knowledge_base[question.lower()].append(response)
    else:
        knowledge_base[question.lower()] = [response]
    print("Terima kasih telah mengajari saya!")

def learn_new_response(question):
    print("Maaf, saya tidak tahu jawaban atas pertanyaan tersebut.")
    response = input("Apa tanggapan yang sesuai? ")
    teach_new_response(question, response)

def chat():
    print("Halo! Saya adalah chatbot sederhana. Ada yang bisa saya bantu?")
    while True:
        user_input = input("Anda: ").lower()
        if user_input in greetings:
            print("ChatBot:", respond_to_greeting())
        elif user_input in farewells:
            print("ChatBot:", respond_to_farewell())
            break
        else:
            response = respond_to_question(user_input)
            print("ChatBot:", response)
            if response in fallback_response:
                learn_new_response(user_input)

if __name__ == "__main__":
    chat()
