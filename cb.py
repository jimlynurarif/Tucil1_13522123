import time
import random

def generate_patterns(n, m, max_len, buffer_size):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, left, down, up directions
    patterns = []

    def search(x, y, path, change_dir, preddx, preddy):
        if len(path) > max_len:
            return
        patterns.append(path[:])
        for i in range(4):
            dx, dy = directions[i]
            nx, ny = x + dx, y + dy 
            if (len(path) > 1 or (dx, dy) == (1, 0)) and 0 <= nx < n and 0 <= ny < m and (nx, ny) not in path  and change_dir < buffer_size:
                if (preddx == dx or preddy == dy):
                    path.append((nx, ny))
                    search(nx, ny, path, change_dir, dx, dy)
                else:
                    path.append((nx, ny))
                    search(nx, ny, path, change_dir + 1, dx, dy)
                path.pop()

    search(0, 0, [(0, 0)], 1, 0, 0)

    return patterns

def deletePath(patterns):
  for i in range(len(patterns)):
    coordinates = patterns[i]
    j = 1
    while j < len(coordinates) - 1:
        if coordinates[j][1] == coordinates[j - 1][1] and coordinates[j][1] == coordinates[j + 1][1]:
            del coordinates[j]
        elif coordinates[j][0] == coordinates[j - 1][0] and coordinates[j][0] == coordinates[j + 1][0]:
            del coordinates[j]
        else:
            j += 1
  return patterns

# patterns = generate_patterns(10,10,13) #contoh patterns [[(0, 0)], [(0, 0), (0, 1)], [(0, 0), (0, 1), (0, 2)]]
# deletePath(patterns)
# print(patterns)

# masukan ke file
# with open("adam.txt", "w") as file:
#   for pattern in patterns:
#     file.write(str(pattern) + "\n")

def developer_sequences_build():
  sequences = [
      ['BD', 'E9', '1C'],
      ['BD', '7A', 'BD'],
      ['BD', '1C', 'BD', '55']
  ]
  sequences_rewards = [10, 20, 30]
  return sequences, sequences_rewards

def count_point(all_path, sequences, sequences_rewards):
    # Inisialisasi array path_reward dengan nilai nol
    path_reward = [0] * len(all_path)

    # Iterasi melalui setiap jalur dan setiap urutan
    for i, path in enumerate(all_path):
        used_index = []
        for j in range(len(path) - 1):
            for k in range(j + 1, len(path)):
                sequence = path[j:k + 1]
                if sequence in sequences:
                    # Dapatkan indeks dari sequence dalam sequences
                    index = sequences.index(sequence)
                    # Jika indeks belum ada dalam used_index, tambahkan nilai dari sequences_rewards
                    if index not in used_index:
                        path_reward[i] += sequences_rewards[index]
                        # Tambahkan indeks ke used_index
                        used_index.append(index)

    return path_reward

def path_biggest_point(path_reward, all_path):
    biggest = max(path_reward)
    if biggest == 0:
        return "none","none"
    index = path_reward.index(biggest)
    path = all_path[index]

    return path, biggest, index

def sequences_build():
    number_of_sequences = int(input("Enter the number of sequences: "))
    sequences = []
    sequences_rewards = []
    for i in range(number_of_sequences):
        sequence = input("Enter the sequence {}: ".format(i + 1)).strip().split()
        # Pastikan sequence memiliki minimal dua elemen
        while len(sequence) < 2:
            print("Sequence harus terdiri dari minimal dua elemen. Coba lagi.")
            sequence = input("Enter the sequence {}: ".format(i + 1)).strip().split()
        sequences.append(sequence)
        sequences_reward = int(input("Enter the reward for sequence {}: ".format(i + 1)))
        sequences_rewards.append(sequences_reward)
    return sequences, sequences_rewards


def extractPath(results, matrix):
    all_path = []
    for i in range(len(results)):
        coordinates = results[i]
        values = [matrix[row][col] for row, col in coordinates]
        all_path.append(values)
    return all_path

def matrix_build():
    matrix_dimensions = input("matrix_width matrix_height: ").split()
    matrix_width = int(matrix_dimensions[1])
    matrix_height = int(matrix_dimensions[0])
    matrix = [[0 for i in range(matrix_width)] for j in range(matrix_height)]
    matrix = []
    print("Masukkan matriks (pisahkan elemen dengan spasi, baris baru untuk setiap baris):")
    for _ in range(matrix_height): 
        row = input().strip().split()
        while len(row) != matrix_width:
            print("Error: Jumlah elemen harus sama jumlah kolom!!!")
            print("Ulangi input baris terkini: ")
            row = input().strip().split()
        matrix.append(row)
    return matrix_width, matrix_height, matrix

import random

def generate_random_sequences(token):
    sequences = []
    sequences_rewards = []
    jumlah_sekuens = int(input("jumlah sekuens: "))
    ukuran_maksimal_sekuens = int(input("ukuran maksimal sekuens: "))

    for _ in range(jumlah_sekuens):
        sequence_length = random.randint(2, ukuran_maksimal_sekuens)
        sequence = [random.choice(token) for _ in range(sequence_length)]
        
        sequences.append(sequence)
        sequences_rewards.append(random.randint(1, 30))

    return sequences, sequences_rewards

def matrix_generator(token, n, m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(random.choice(token))
        matrix.append(row)
    return matrix

def main():
    method = input("Masukkan metode input (manual/auto): ")
    if method == "manual":
        buffer_size = int(input("Masukkan buffer size: "))
        matrix_width, matrix_height, matrix = matrix_build() # manually
        max_len = matrix_width * matrix_height
        sequences, sequences_rewards = sequences_build() # manually
        print("loading... too big buffer_size can take a long time, please sabar \n")
        start_time = time.time()
        patterns = generate_patterns(matrix_height, matrix_width, max_len, buffer_size)
        patterns = deletePath(patterns)
        results = extractPath(patterns, matrix)
        # with open("adam.txt", "w") as file:
        #     for result in results:
        #         file.write(str([result]) + "\n")
        path_reward = count_point(results, sequences, sequences_rewards)
        path, biggest, path_biggest_index = path_biggest_point(path_reward, results)
        biggest_path_Windexes = patterns[path_biggest_index]
        end_time = time.time()
        runtime = round((end_time - start_time) * 1000)
        print("biggest score = ", biggest)
        # print(path)
        print("path: ", end="")
        for i in range(len(path)):
            print(path[i], end=" ")
        print('''

koordinat path
baris, kolom''')
        for point in biggest_path_Windexes:
            print(f"{point[0]}, {point[1]}")
        print("\n" + str(runtime) + " ms")
        is_save = input("Apakah ingin menyimpan hasil ke file? (y/n): ")
        # simpan tanpa prompt
        if is_save == "y":
            with open("result.txt", "w") as file:
                file.write(str(biggest) + "\n")
                for i in range(len(path)):
                    file.write(str(path[i]) + " ")
                file.write("\n")
                for point in biggest_path_Windexes:
                    file.write(f"{point[0]}, {point[1]}\n")
                file.write("\n" + str(runtime) + " ms")
            print("Berhasil disimpan di result.txt")
        # sequences, sequences_rewards = developer_sequences_build()
        # path_reward = count_point(results, sequences, sequences_rewards)
        # print(path_reward)
        # path, biggest = path_biggest_point(path_reward, results)
        # print("biggest score = ", biggest)
        # print(path)
        # end_time = time.time()
        # runtime = end_time - start_time
        # print(runtime, "ms")
    elif method == "auto":
        jumlah_token_unik = int(input("Masukkan jumlah token unik: "))
        token = input("Masukkan token: ").split() # misal bentuknya kek gini ['E9', 'B7', '8M']
        while len(token) != jumlah_token_unik:
            print("Error: Jumlah token harus", jumlah_token_unik, "!!!")
            print("Ulangi input baris terkini: ")
            token = input().strip().split()
        buffer_size = int(input("buffer size: "))
        matrix_dimensions = input("matrix_height matrix_width: ").split()
        matrix_height = int(matrix_dimensions[0])
        matrix_width = int(matrix_dimensions[1])
        print("loading... too big buffer_size can take a long time, please sabar \n")
        max_len = matrix_width * matrix_height
        sequences, sequences_rewards = generate_random_sequences(token)
        matrix = matrix_generator(token, matrix_height, matrix_width)
        for _ in range(len(matrix)):
            print(matrix[_])
        print("sequences: ", sequences)
        print("sequences_rewards: ", sequences_rewards)
        start_time = time.time()
        patterns = generate_patterns(matrix_height, matrix_width, max_len, buffer_size)
        patterns = deletePath(patterns)
        results = extractPath(patterns, matrix)
        path_reward = count_point(results, sequences, sequences_rewards)
        # print("path_reward:", path_reward)
        path, biggest, path_biggest_index = path_biggest_point(path_reward, results)
        biggest_path_Windexes = patterns[path_biggest_index]
        end_time = time.time()
        runtime = round((end_time - start_time) * 1000)
        print("biggest score = ", biggest)
        # print(path)
        print("path: ", end="")
        for i in range(len(path)):
            print(path[i], end=" ")
        print('''

koordinat path
baris, kolom''')
        for point in biggest_path_Windexes:
            print(f"{point[0]}, {point[1]}")
        print("\n" + str(runtime) + " ms")

        is_save = input("Apakah ingin menyimpan hasil ke file? (y/n): ")
        # simpan tanpa prompt
        if is_save == "y":
            with open("result.txt", "w") as file:
                file.write(str(biggest) + "\n")
                for i in range(len(path)):
                    file.write(str(path[i]) + " ")
                file.write("\n")
                for point in biggest_path_Windexes:
                    file.write(f"{point[0]}, {point[1]}\n")
                file.write("\n" + str(runtime) + " ms")
            print("Berhasil disimpan di result.txt")
    else:
        print("Invalid method input")
        main()

if __name__ == "__main__":
    main()