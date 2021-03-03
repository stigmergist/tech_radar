import os
import yaml

path = '.././data'

categories = set()

for root, d_names, f_names in os.walk(path):
    for p in (os.path.join(root, file) for file in f_names if file.endswith('.yaml')):
        with open(p,'r') as file:
            spec = yaml.load(file, Loader=yaml.FullLoader)
            for cat in spec['categories']: categories.add(cat)

print(categories)
