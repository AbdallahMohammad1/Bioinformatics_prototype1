from collections import Counter
from standards import DNA_Codons,RNA_Codons
class Feature():
    def nucleotide_frequency(self,seq):
        """Count nucleotides in a given sequence. Return a dictionary"""
        freqs=dict(Counter(seq))
        freqs.popitem()
        return freqs
    def transcription(self,seq):
        """DNA -> RNA Transcription. Replacing Thymine with Uracil"""
        return seq.replace("T", "U")
    def reverse_complement(self,seq,seq_type):
        """
        Swapping adenine with thymine and guanine with cytosine.
        Reversing newly generated string
        """
        if seq_type == "DNA":
            mapping = str.maketrans('ATCG', 'TAGC')
        else:
            mapping = str.maketrans('AUCG', 'UAGC')
        return seq.translate(mapping)[::-1]
    def gc_content(self,seq):
        """GC Content in a DNA/RNA sequence"""
        return round((seq.count('C') + seq.count('G')) / len(seq) * 100)
    def translate_seq(self,seq,seq_type, init_pos=0):
        """Translates a DNA sequence into an aminoacid sequence"""
        if seq_type == "DNA":
            return [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) - 2, 3)]
        elif seq_type == "RNA":
            return [RNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) - 2, 3)]
    def codon_usage(self,seq,seq_type, aminoacid):
        """Provides the frequency of each codon encoding a given aminoacid in a DNA sequence"""
        list_amino = []
        if seq_type == "DNA":

            for i in range(0, len(seq) - 4, 3):
                if DNA_Codons[seq[i:i + 3]] == aminoacid:
                    print(seq[i:i + 3])
                    list_amino.append(seq[i:i + 3])
        elif seq_type == "RNA":
            for i in range(0, len(seq) - 4, 3):
                if RNA_Codons[seq[i:i + 3]] == aminoacid:
                    list_amino.append(seq[i:i + 3])

        freqDict = dict(Counter(list_amino))
        totalWight = sum(freqDict.values())
        for i in freqDict:
            freqDict[i] = round(freqDict[i] / totalWight, 2)
        return freqDict
        #return list_amino