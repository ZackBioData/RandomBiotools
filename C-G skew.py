def min_skew_positions(genome):
    skew = [0]  # Skew starts at 0 at position 0
    
    # Compute skew values across the genome
    for nucleotide in genome:
        if nucleotide == 'G':
            skew.append(skew[-1] + 1)
        elif nucleotide == 'C':
            skew.append(skew[-1] - 1)
        else:
            skew.append(skew[-1])  # No change for A or T

    # Find the minimum skew value
    min_skew_value = min(skew)

    # Get all positions where the skew is at minimum
    min_positions = [i for i, value in enumerate(skew) if value == min_skew_value]
    
    # Print both the minimum skew value and positions
    print(f"Minimum skew value: {min_skew_value}")
    print("Positions with minimum skew:", " ".join(map(str, min_positions)))

    return min_positions

# Sample Input
genome = "GCATACACTTCCCAGTAGGTACTG"

# Get minimum skew positions
result = min_skew_positions(genome)
