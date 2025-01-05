from app import db, Question
from app import app

# Uygulama bağlamı içinde veritabanı işlemi yapalım
with app.app_context():
    db.create_all()  # Veritabanı tablolarını oluşturma

    # Soruları ekleme
    q1 = Question(question_text="Python'da AI için en popüler kütüphane nedir?",
                  option1="NumPy", option2="Pandas", option3="TensorFlow", option4="Matplotlib", correct_option=3)
    q2 = Question(question_text="Python'da AI geliştirme için kullanılan bir veri analizi kütüphanesi hangisidir?",
                  option1="Keras", option2="Pandas", option3="BeautifulSoup", option4="Django", correct_option=2)
    q3 = Question(question_text="Bilgisayar görüşüyle hangi işlemler yapılabilir?",
                  option1="Yüz tanıma", option2="Oyunlar geliştirmek", option3="Ses tanıma", option4="Metin analizleri", correct_option=1)
    q4 = Question(question_text="OpenCV'nin amacı nedir?",
                  option1="Sesli komutları analiz etmek", option2="Veri güvenliğini sağlamak", option3="Web sayfaları oluşturmak", option4="Görüntü işleme ve analiz", correct_option=4)
    q5 = Question(question_text="NLP'de hangi model yaygın olarak kullanılır?",
                  option1="TensorFlow", option2="OpenCV", option3="GPT", option4="Pandas", correct_option=3)

    db.session.add_all([q1, q2, q3, q4, q5])
    db.session.commit()  # Değişiklikleri veritabanına kaydet
    print("Sorular başarıyla eklendi.")
