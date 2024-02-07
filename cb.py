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

  rows = 3
  cols = 3

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


def array_possible_routes(matrix, buffer_size):
  # return possible of routes, first element of route must be in the first row of the matrix, second element must be second row (below the first element), and the maximum length of the route is buffer_size, the route must be alternately horizontal and vertical
  def is_valid_position(row, col):
      return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

  def is_valid_move(row, col, prev_row, prev_col):
      return abs(row - prev_row) + abs(col - prev_col) == 1 and (row != prev_row or col != prev_col) and (abs(row - col) < 2)

  def find_routes(row, col, path, routes):
      if len(path) > buffer_size:
          return
      path.append((row, col))
      routes.append(path[:])

      for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
          next_row, next_col = row + dr, col + dc
          if is_valid_position(next_row, next_col) and is_valid_move(next_row, next_col, row, col):
              find_routes(next_row, next_col, path, routes)

      path.pop()

  routes = []
  for col in range(len(matrix[0])):
      find_routes(0, col, [], routes)
  return routes
  


if __name__ == "__main__":
  buffer_size = 7
  print(developer_matrix_build())
  matrix = developer_matrix_build()
  developer_sequences_build()
  print("A")
  print(array_possible_routes(matrix, buffer_size))
