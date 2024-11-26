# Problem 3

def count_min_sketch(a, b, p, w, stream):
    """
    Implements the Count-Min Sketch.

    Parameters:
    - a: list of integers, coefficients for the hash functions
    - b: list of integers, offsets for the hash functions
    - p: int, a large prime number
    - w: int, the width of the sketch matrix
    - stream: iterator producing the stream of data

    Returns:
    - sketch_matrix: list of lists (d x w), the Count-Min Sketch matrix
    """

    d = len(a)  

    sketch_matrix = [[0] * w for _ in range(d)]

    for x in stream:
        for i in range(d):
            hash_value = ((a[i] * x + b[i]) % p) % w
            sketch_matrix[i][hash_value] += 1

    return sketch_matrix
