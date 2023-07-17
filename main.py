def init_matrix(rows, cols):
    return [[0 for j in range(cols)] for i in range(rows)]


def score_cell(char1, char2, match, mismatch):
    if char1 == char2:
        return match
    else:
        return mismatch


def max_score(left, top, diagonal, gap):
    return max(left + gap, top + gap, diagonal)


def compute_matrix(seq1, seq2, match, mismatch, gap):
    rows = len(seq1) + 1
    cols = len(seq2) + 1
    matrix = init_matrix(rows, cols)

    for i in range(1, rows):
        matrix[i][0] = matrix[i - 1][0] + gap
    for j in range(1, cols):
        matrix[0][j] = matrix[0][j - 1] + gap

    for i in range(1, rows):
        for j in range(1, cols):
            score = score_cell(seq1[i - 1], seq2[j - 1], match, mismatch)
            matrix[i][j] = max_score(matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1] + score, gap)

    return matrix

def generate_alignment(seq1, seq2, matrix, match, mismatch, gap):
    align1 = ""
    align2 = ""
    i = len(seq1)
    j = len(seq2)

    while i > 0 or j > 0:
        if i > 0 and j > 0 and matrix[i][j] == matrix[i - 1][j - 1] + score_cell(seq1[i - 1], seq2[j - 1], match,
                                                                                 mismatch):
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            i -= 1
            j -= 1
        elif i > 0 and matrix[i][j] == matrix[i - 1][j] + gap:
            align1 = seq1[i - 1] + align1
            align2 = "-" + align2
            i -= 1
        else:
            align1 = "-" + align1
            align2 = seq2[j - 1] + align2
            j -= 1

    return align1, align2


seq1 = input("Enter the first DNA sequence: ")
seq2 = input("Enter the second DNA sequence: ")
match = int(input("Enter the match score: "))
mismatch = int(input("Enter the mismatch score: "))
gap = int(input("Enter the gap penalty score: "))

matrix = compute_matrix(seq1, seq2, match, mismatch, gap)
align1, align2 = generate_alignment(seq1, seq2, matrix, match, mismatch, gap)

print("Matrix:")
for row in matrix:
    print(row)

print("Alignment:")
print(align1)
print(align2)
