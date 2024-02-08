def extract_elements(matrix, coordinates):
    result = []
    for coord in coordinates:
        row, col = coord
        result.append(matrix[row][col])
    return result

# Contoh matriks
matrix = [
    ['U9', '79', 'A8'],
    ['M5', 'U7', 'F9'],
    ['G7', 'H6', '2I']
]

# Koordinat yang ingin diekstrak
coordinates = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)]

# Ekstrak elemen dan gabungkan menjadi daftar
result_list = extract_elements(matrix, coordinates)

print(result_list)  # Output: ['U9', 'M5', 'U7', 'H6', '2I']
