dna = 'ATGCATGCTAGCATGCTAGCTAGCTA'

k = 3
kmer_count = {}
for start in range(len(dna) -k+1):
    kmer = dna[start:start +k]
    mevcut_sayi = kmer_count.get(kmer, 0)
    kmer_count[kmer] = mevcut_sayi+1
    print(kmer_count)