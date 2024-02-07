#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <ctime>

using namespace std;

// Fungsi untuk menghasilkan karakter alfanumerik dua karakter secara acak
string generateRandomAlphaNumeric() {
    const string alphanum = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string result = "";
    for (int i = 0; i < 2; ++i) {
        result += alphanum[rand() % alphanum.size()];
    }
    return result;
}

int main() {
    

    srand(time(0)); // Inisialisasi seed untuk menghasilkan angka acak

    int rows, cols;

    cout << "Masukkan jumlah baris matriks: ";
    cin >> rows;
    cout << "Masukkan jumlah kolom matriks: ";
    cin >> cols;

    // Membuat matriks dengan ukuran yang telah dimasukkan
    string **matrix = new string*[rows];
    for (int i = 0; i < rows; ++i) {
        matrix[i] = new string[cols];
    }

    // Mengisi matriks dengan karakter alfanumerik acak
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            matrix[i][j] = generateRandomAlphaNumeric();
        }
    }

    // Menampilkan matriks
    cout << "Matriks dengan isi acak alfanumerik dua karakter:\n";
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            cout << setw(3) << matrix[i][j] << " ";
        }
        cout << endl;
    }

    // Menghapus matriks dari memori
    for (int i = 0; i < rows; ++i) {
        delete[] matrix[i];
    }
    delete[] matrix;

    return 0;
}
