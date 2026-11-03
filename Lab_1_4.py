import math
from functools import reduce

# Lambda for normalization
min_max_norm = lambda x, mn, mx: (x - mn) / (mx - mn)
data = [10, 25, 5, 40, 15, 30]
min_v, max_v = min(data), max(data)
normalized = [round(min_max_norm(x, min_v, max_v), 4) for x in data]
print('Normalized:', normalized)

# List comprehension with condition (feature filter)
feature_matrix = [[0.1, -0.5, 2.3], [0.8, 1.2, -0.1], [3.1, 0.4, 0.9]]
filtered = [row for row in feature_matrix if max(row) < 3.0]
print('Filtered rows:', filtered)

# Dict comprehension for label encoding
labels = ['cat', 'dog', 'car', 'cat', 'dog']
unique_labels = sorted(set(labels))
encoder = {label: idx for idx, label in enumerate(unique_labels)}
encoded = [encoder[l] for l in labels]
print('Encoder:', encoder)
print('Encoded:', encoded)

# Reduce for cumulative product (learning rate schedule)
lr_decay = [0.9, 0.9, 0.9, 0.9, 0.9]
final_lr = 0.01 * reduce(lambda a, b: a * b, lr_decay)
print(f'LR after 5 epochs: {final_lr:.6f}')