import random
import string

def matrix_build():
  matrix_width = int(input("Masukkan jumlah kolom: "))
  matrix_height = int(input("Masukkan jumlah baris: "))
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

def sequences_build():
  number_of_sequences = int(input("Enter the number of sequences: "))
  sequences = []
  sequences_rewards = []
  for i in range(number_of_sequences):
      sequence = input("Enter the sequence: ").strip().split()
      sequences.append(sequence)
      sequences_reward = int(input("Enter the reward for sequence {}: ".format(i + 1)))
      sequences_rewards.append(sequences_reward)
  return sequences, sequences_rewards


def developer_matrix_build():
  class AlphanumericMatrix:
      def __init__(self, rows, cols):
          self.rows = rows
          self.cols = cols
          self.matrix = [[self.generate_random_alphanumeric() for _ in range(cols)] for _ in range(rows)]

      def generate_random_alphanumeric(self):
          alphanumeric_chars = string.digits + string.ascii_uppercase
          return ''.join(random.choice(alphanumeric_chars) for _ in range(2))

      def display_matrix(self):
          for row in self.matrix:
              print(' '.join(row))

  rows = 8
  cols = 8

  alphanumeric_matrix = AlphanumericMatrix(rows, cols)
  # print("Matriks: ")
  # alphanumeric_matrix.display_matrix()
  # print(alphanumeric_matrix.matrix)
  return alphanumeric_matrix.matrix

def developer_sequences_build():
  sequences = [
      ['U9', '79', 'A8'],
      ['M5', 'U7', 'F9'],
      ['G7', 'H6', '2I']
  ]
  sequences_rewards = [10, 20, 30]
  return sequences, sequences_rewards


def generate_patterns(n, m, max_len):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, left, down, up directions
    patterns = []

    def dfs(x, y, path, direction_index):
        if len(path) > max_len:
            return
        patterns.append(path[:])
        for i in range(2):
            dx, dy = directions[direction_index + i]
            nx, ny = x + dx, y + dy 
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in path:
                path.append((nx, ny))
                dfs(nx, ny, path, (direction_index + 2) % 4)  # Alternate between vertical and horizontal
                path.pop()

    for i in range(m):
        dfs(0, i, [(0, i)], 2)  # Start with downward movement, 2 is the index of downward movement, see directions array

    return patterns

def extract_elements(matrix, coordinates):
    result = []
    for coord_list in coordinates:
        temp_result = []
        for coord in coord_list:
            row, col = coord
            temp_result.append(matrix[row][col])
        result.append(temp_result)
    return result

if __name__ == "__main__":
  buffer_size = 10
  matrix_width, matrix_height, matrix = matrix_build()
  patterns = generate_patterns(matrix_height, matrix_width, buffer_size)
  developer_sequences_build()
  print("A")
  result_list = extract_elements(matrix, patterns)
  print(result_list)
