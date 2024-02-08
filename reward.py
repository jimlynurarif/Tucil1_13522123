def count_point(all_path, sequences, sequences_rewards):
    # Inisialisasi array path_reward dengan nilai nol
    path_reward = [0] * len(all_path)

    # Iterasi melalui setiap jalur dan setiap urutan
    for i, path in enumerate(all_path):
        for sequence in sequences:
            if path == sequence:
                # Jika jalur ada dalam urutan, tambahkan nilai dari sequences_rewards
                path_reward[i] += sequences_rewards[sequences.index(sequence)]

    return path_reward

# Contoh penggunaan
all_path = ["A", "B", "C", "D"]
sequences = ["B", "D", "A"]
sequences_rewards = [10, 20, 30]

result = count_point(all_path, sequences, sequences_rewards)
print("Skor setiap jalur:", result)
