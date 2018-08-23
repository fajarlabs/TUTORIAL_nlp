# Environment
pastikan JAVAHOME sudah di set terlebih dahulu

# Cara untuk training sebagai berikut
# jika heapspace bisa disetting dengan konfigurasi yang lain
java -cp "*" -mx4g edu.stanford.nlp.ie.crf.CRFClassifier -prop train/prop.txt
# cara untuk test model
java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier your_classifier.ser.gz -testFile your_output.txt
# taruh classifier sesuai path pada program
# cara menjalankan sebagai berikut
python contoh_nertagger.py