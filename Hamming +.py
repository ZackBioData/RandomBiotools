from itertools import product

# Function to compute the reverse complement of a DNA sequence
def reverse_complement(pattern):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join(complement[base] for base in reversed(pattern))

# Compute Hamming distance between two strings
def hamming_distance(p1, p2):
    return sum(1 for a, b in zip(p1, p2) if a != b)

# Generate all possible k-mers within d mismatches
def neighbors(pattern, d):
    nucleotides = ['A', 'C', 'G', 'T']
    pattern_list = list(pattern)
    neighborhood = set()
    
    # Generate all possible k-mers by changing up to d positions
    for positions in product(range(len(pattern)), repeat=d):
        for replacements in product(nucleotides, repeat=d):
            mutated = pattern_list[:]
            for pos, new_char in zip(positions, replacements):
                mutated[pos] = new_char
            neighborhood.add("".join(mutated))
    
    return neighborhood | {pattern}

# Main function to find frequent k-mers with mismatches & reverse complements
def frequent_words_with_mismatches_and_rc(text, k, d):
    freq_map = {}
    
    # Iterate over all k-mers in the text
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        pattern_rc = reverse_complement(pattern)
        
        # Get all neighbors (mutations within d mismatches)
        neighborhood = neighbors(pattern, d) | neighbors(pattern_rc, d)
        
        for neighbor in neighborhood:
            freq_map[neighbor] = freq_map.get(neighbor, 0) + 1
    
    # Find max frequency
    max_count = max(freq_map.values(), default=0)
    
    # Get all k-mers with the max count
    return [kmer for kmer, count in freq_map.items() if count == max_count]

# Example Usage
text = "AAATGAAAATAAGTGAACTGTACACGTCATACTGTCATACTACTCAACGACGTGACGACGACGGCGCACGTCAACGTCAACGTACACGACGGCTACACGTCATACTCAGCACGTCAGCTACTACGCACGGCTACGCTGTACTCAACGTCATACTGTCATACGCTGTACACGACGTGACGTCAGCGCTACTGACGACGTGACGTCATGGCTCATACGCACGTCAACGGCTACTGTCAACGACGGCGCTGGCACGTGACGAAATGAGTGCAACAAGTGAAATATATGTGCAAATGTGCAACAAATGTGGTGGTGGAAAATATAAGTGAACAAATAAGTGCAAGTGCAAGTGAAATAAGTGGTGAAGAGTGATCAAGTGATGAGTGCAAGAATGACAACAAAAGTGATGAATAACAAAACAACAAAAGAAAATGAATATGAATGAAAGA"
k, d = 6, 2
result = frequent_words_with_mismatches_and_rc(text, k, d)
print(" ".join(result))
