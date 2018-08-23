from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
text = 'Corpus, jamak dari corpora; Sebuah koleksi data linguistik, baik disusun sebagai teks-teks tertulis atau sebagai sebuah transkripsi rekaman suara. Tujuan utama dari corpus adalah untuk memverifikasi sebuah hipotesis tentang bahasa - misalnya, untuk menentukan bagaimana penggunaan suara tertentu, kata atau ragam susunan sintaksis. Linguistik Corpus berkaitan dengan prinsip-prinsip dan praktik menggunakan corpora dalam studi bahasa. Korpus komputer adalah bagian besar teks-teks yang dapat dibaca mesin.'
stop_words = set(stopwords.words('indonesian'))
words = word_tokenize(text)
 
new_sentence = []
 
for word in words:
    if word not in stop_words:
    	new_sentence.append(word)
print(new_sentence)