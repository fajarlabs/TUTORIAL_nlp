#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk.tag import CRFTagger
 
jumSample = 500000
# Menggunakan format dari Fam Rashel yang standard dari stanford
namaFile = "TRAIN_DATA_FORMAT_STANDFORD/ID/idn-tagged-corpus/Indonesian_Manually_Tagged_Corpus.tsv"
with open(namaFile, 'r') as f:
    lines = f.read().split('\n')
 
pasangan = []
allPasangan = []
 
for line in lines[: min(jumSample, len(lines))]:
    if line == '':
        allPasangan.append(pasangan)
        pasangan = []
    else:
        kata, tag = line.split('\t')
        # convert to unicode
        p = (kata.decode('utf-8'),tag.decode('utf-8'))
        pasangan.append(p)
 
ct = CRFTagger()

# output hasilnya dengan extensi tagger
ct.train(allPasangan,'all_indo_man_tag_corpus_model.crf.tagger')

#test hasil trainingnya
hasil = ct.tag_sents([[u'Saya',u'bekerja',u'di',u'Jakarta'],[u'Nama',u'saya',u'Fajar']])

# hasil seperti berikut
print(hasil)