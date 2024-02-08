def extract_elements(matrix, coordinates):
    result = []
    for coord_list in coordinates:
        temp_result = []
        for coord in coord_list:
            row, col = coord
            temp_result.append(matrix[row][col])
        result.append(temp_result)
    return result

# Contoh matriks
matrix = [
    ['U9', '79', 'A8'],
    ['M5', 'U7', 'F9'],
    ['G7', 'H6', '2I']
]

# Koordinat yang ingin diekstrak
coordinates = [[(0, 0)], [(0, 0), (1, 0)], [(0, 0), (1, 0), (1, 1)], [(0, 0), (1, 0), (1, 1), (2, 1)]]

# Ekstrak elemen dan gabungkan menjadi daftar
result_list = extract_elements(matrix, coordinates)

print(result_list)  # Output: [['U9'], ['U9', 'M5'], ['U9', 'M5', 'U7'], ['U9', 'M5', 'U7', 'H6']]
