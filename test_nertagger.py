#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
import nltk.tag.stanford as st
st = st.StanfordNERTagger('standford-ner/classifiers/Indonesian_Manually_Tagged_Corpus_ID.ser.gz', 'standford-ner/stanford-ner.jar') 
text = """
Setelah itu, mereka masuk ke Jalan Raya Campaka-Ramayana Sadang, Kabupaten Purwakarta. Kemudian putar balik ke Jalan Campaka-Cipeundeuy-Kalijati-Otto Iskandardinata-Ahmad Yani-Jalan Raya Cijambe dan finish di Kantor Kecamatan Jalan Cagak.
Harian Detik hari melaporkan ASIAN GAMES yang diselenggarakan di indonesia, dan pada acara balap sepeda dengan route karawang purwakarta subang dengan titik lokasi -6.571589, 107.758736.
Di awal balapan, pebalap Indonesia, Aiman Cahyadi, Jamal Hibatullah, Dadi Suryadi, dan Robin Manullang sudah keteteran bersaing dengan pebalap lain. Mereka harus mengakui keunggulan dari pebalap Kazakhstan, Korea Selatan, Jepang dan negara lainnya.
Memasuki 10 km terakhir, atlet Indonesia mencoba mempercepat laju sepedanya. Tapi, lagi-lagi tidak bisa mengimbangi keperkasaan atlet Kazaktan yang memang diunggulkan.
Empat atlet Indonesia akhirnya hanya mampu menyentuh garis finis di urutan kesembilan atas nama Aiman Cahyadi dengan catatan waktu 3 jam 26,1 detik disusul Robin Manullang dengan catatan waktu yang sama.
Sementara, dua pebalap Indonesia lainnya Dadi Suryadi harus puas di urutan 19 dan Jamal Hibatullah di urutan 34 dengan catatan waktu masing-masing 3:27:45 dan 5:30:40. 
"""
unicode(text, errors='ignore')
for sent in nltk.sent_tokenize(unicode(text, errors='ignore')):
    tokens = nltk.tokenize.word_tokenize(sent)
    tags = st.tag(tokens)
    for tag in tags:
    	print(tag)
        if tag[1]=='PERSON': print tag
        if tag[1]=='LOCATION': print tag
        if tag[1]=='ORGANIZATION': print tag
        if tag[1]=='TIME': print tag
        if tag[1]=='NUMBER': print tag
        if tag[1]=='REGION': print tag
        if tag[1]=='COORDINATES': print tag
        if tag[1]=='CITY': print tag
        if tag[1]=='STREET': print tag