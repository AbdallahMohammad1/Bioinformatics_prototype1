from collections import Counter
class Feature():
    def nucleotide_frequency(self,seq):
        """Count nucleotides in a given sequence. Return a dictionary"""
        freqs=dict(Counter(seq))
        freqs.popitem()
        return freqs