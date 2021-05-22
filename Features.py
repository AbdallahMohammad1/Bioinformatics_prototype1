from collections import Counter
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