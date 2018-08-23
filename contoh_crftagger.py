import nltk
from nltk.tag import CRFTagger
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
import unicodedata
from nltk.probability import FreqDist
from nltk.stem import SnowballStemmer

text = 'Bencana gempa di Lombok menggugah JNE untuk memberikan bantuan dengan mendirikan Posko Bencana JNE Mataram di Kantor JNE Mataram, Jl. Amir Hamzah No. 102 Mataram Lombok Nusa Tenggara Barat. Agar lebih maksimal, JNE mengajak masyarakat di seluruh Indonesia untuk menyumbangkan beragam barang yang diperlukan oleh masyarakat di Lombok yang terdampak bencana gempa bumi.'

# ---------------------------------------------------------------|
# untuk menghilangkan kata yang tidak perlu
# ---------------------------------------------------------------|
stop_words = set(stopwords.words('indonesian'))
words = word_tokenize(text)
 
new_sentence = []
 
for word in words:
    if word not in stop_words:
    	new_sentence.append(word)
 
new_sentence = [unicode(new_sentence[x], "utf-8") for x in range(len(new_sentence))]

ct = CRFTagger()
ct.set_model_file('all_indo_man_tag_corpus_model.crf.tagger')
hasil = ct.tag_sents([new_sentence])

# ---------------------------------------------------------------|
# untuk melihat frekuensi kata yang muncul
# ---------------------------------------------------------------|
# fdist = FreqDist(new_sentence)
# print(fdist.most_common())

# ---------------------------------------------------------------|
# untuk melihat frekuensi kata yang muncul
# ---------------------------------------------------------------|
# for tokenTag in hasil[0]:
#     token, tag = tokenTag;
#     token_text = unicodedata.normalize(u'NFKD', token).encode(u'ascii',u'ignore')
#     print(token_text,"->",tag);

# ----------------------------------------------------------------------------|
# Stemming merupakan suatu proses untuk menemukan kata dasar dari sebuah kata
# ----------------------------------------------------------------------------|
snowball_stemmer = SnowballStemmer("english")
print(snowball_stemmer.stem('probability'))