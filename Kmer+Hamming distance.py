def hamming_distance(p, q):
    """Compute the Hamming distance between two equal-length strings."""
    return sum(1 for i in range(len(p)) if p[i] != q[i])

def approximate_pattern_matching(pattern, text, d):
    """Find all starting positions where pattern appears in text with at most d mismatches."""
    pattern_length = len(pattern)
    positions = []  # List to store the valid starting indices

    # Ensures that we don’t go out of bounds when extracting substrings
    for i in range(len(text) - pattern_length + 1):
        # Extracts the k-mer (substring of length pattern_length) starting at position i
        substring = text[i:i + pattern_length]
        
        # Computes the Hamming distance between pattern and the extracted substring
        # Checks if the mismatch count (≤ d) is within the allowed limit
        if hamming_distance(pattern, substring) <= d:
            positions.append(i)  # Adds position i to the list
           
    return positions

# Sample Input
pattern = "CCC"
text = "CATGCCATTCGCATTGTCCCAGTGA"
d = 2

# Compute Approximate Pattern Matches
result = approximate_pattern_matching(pattern, text, d)

# Print output as space-separated indices
print(" ".join(map(str, result)))
print(f"Quantity = {len(result)}")
