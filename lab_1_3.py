# Nested dataset schema
dataset = {
    'metadata': {'name': 'ImageNet-Mini', 'version': '2.1', 'classes': 10},
    'splits': {
        'train': {'samples': 8000, 'path': '/data/train'},
        'val': {'samples': 1000, 'path': '/data/val'},
        'test': {'samples': 1000, 'path': '/data/test'}
    },
    'class_distribution': {'cat': 1200, 'dog': 1100, 'car': 950}
}

# Nested access
print('Dataset:', dataset['metadata']['name'])
print('Train samples:', dataset['splits']['train']['samples'])

# Dictionary comprehension
normalized = {
    cls: count / sum(dataset['class_distribution'].values())
    for cls, count in dataset['class_distribution'].items()
}
for cls, pct in normalized.items():
    print(f'  {cls}: {pct:.2%}')

# Safe access with .get()
lr = dataset.get('hyperparams', {}).get('learning_rate', 0.001)
print(f'Learning rate: {lr}')