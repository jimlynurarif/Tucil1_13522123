def count_point(all_path, sequences, sequences_rewards):
    # Inisialisasi array path_reward dengan nilai nol
    path_reward = [0] * len(all_path)

    # Iterasi melalui setiap jalur dan setiap urutan
    for i, path in enumerate(all_path):
        for j in range(len(path) - 1):
            sequence = [path[j], path[j + 1]]
            if sequence in sequences:
                # Jika urutan ada dalam sequences, tambahkan nilai dari sequences_rewards
                path_reward[i] += sequences_rewards[sequences.index(sequence)]

    return path_reward