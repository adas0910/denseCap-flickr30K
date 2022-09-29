import json

with open('data/flickr30k_splits.json', 'w') as splits_json:
    splits = {'test': [], 'val': [], 'train': []}
    with open('flickr30k_entities/test.txt', 'r') as test_file, open('flickr30k_entities/train.txt', 'r') as train_file, open('flickr30k_entities/val.txt', 'r') as val_file:
        test = [int(line.strip()) for line in test_file]
        splits['test'] = test
        train = [int(line.strip()) for line in train_file]
        splits['train'] = train
        val = [int(line.strip()) for line in val_file]
        splits['val'] = val
    json.dump(splits, splits_json)
