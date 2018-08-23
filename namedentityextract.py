from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []
    for i in chunked:
            if type(i) == Tree:
                    current_chunk.append(" ".join([token for token, pos in i.leaves()]))
            elif current_chunk:
                    named_entity = " ".join(current_chunk)
                    if named_entity not in continuous_chunk:
                            continuous_chunk.append(named_entity)
                            current_chunk = []
            else:
                    continue
    return continuous_chunk

my_sent = "Bencana gempa di Lombok menggugah JNE untuk memberikan bantuan dengan mendirikan Posko Bencana JNE Mataram di Kantor JNE Mataram, Jl. Amir Hamzah No. 102 Mataram Lombok Nusa Tenggara Barat. Agar lebih maksimal, JNE mengajak masyarakat di seluruh Indonesia untuk menyumbangkan beragam barang yang diperlukan oleh masyarakat di Lombok yang terdampak bencana gempa bumi.."

print(get_continuous_chunks(my_sent))