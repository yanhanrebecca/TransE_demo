import os, random
with open(file="rel_triple.txt") as f:
    lines = f.readlines()
split_index = int(len(lines) * 0.8)
# 随机打乱数据
random.shuffle(lines)
# 划分数据
train_data = lines[:split_index]
test_data = lines[split_index:]
# 将训练集和测试集写入文件
with open('train.txt', 'w', encoding='utf-8') as f:
    f.write(''.join(train_data))

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write(''.join(test_data))

def process_data(file):
    with open(file) as f:
        lines = f.readlines()

    entities = dict()  # 存储头实体与索引
    relations = dict()  # 存储关系与索引

    ent_idx = 0  # 记录当前索引
    rel_idx = 0
    for line in lines:
        items = line.strip().split()
        head = items[0]
        relation = items[1]
        tail = items[2]

        if head not in entities:  # 首次遇到头实体
            entities[head] = ent_idx
            ent_idx += 1

        if tail not in entities:  # 首次遇到尾实体
            entities[tail] = ent_idx
            ent_idx += 1

        if relation not in relations:  # 首次遇到关系
            relations[relation] = rel_idx
            rel_idx += 1
    folder_path = ''
    if file == 'train.txt':
        folder_path = '../data/train'
        os.makedirs(folder_path, exist_ok=True)
    if file == 'test.txt':
        folder_path = '../data/test'
        os.makedirs(folder_path, exist_ok=True)

    with open(folder_path + '/index_rel_triple.txt', 'w') as f:
        for line in lines:
            items = line.strip().split()
            head = items[0]
            relation = items[1]
            tail = items[2]
            f.write(f'{entities[head]}  {relations[relation]}  {entities[tail]}\n')

    """
    实体和关系也可以采用不同的索引空间,保持各自索引的唯一性。
    """

    with open(folder_path + '/all_ent.txt', 'w') as f:
        for key, value in sorted(entities.items(), key=lambda item: item[1]):
            f.write(f'{value}  {key}  \n')

    with open(folder_path + '/all_rel.txt', 'w') as f:
        for key, value in sorted(relations.items(), key=lambda item: item[1]):
            f.write(f'{value}  {key}  \n')


process_data('train.txt')
process_data('test.txt')
