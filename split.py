import os
import shutil
import random

random.seed(42)

base_dir = "Task2/hunt_dataset"
output_dir = "Task2/hunt_dataset_split"

splits = {
    "train": 0.7,
    "val": 0.15,
    "test": 0.15
}

classes = ["hunters", "zombies"]

for split in splits:
    for cls in classes:
        os.makedirs(os.path.join(output_dir, split, cls), exist_ok=True)

for cls in classes:
    images = os.listdir(os.path.join(base_dir, cls))
    random.shuffle(images)

    n_total = len(images)
    n_train = int(n_total * 0.7)
    n_val = int(n_total * 0.15)

    train_imgs = images[:n_train]
    val_imgs = images[n_train:n_train + n_val]
    test_imgs = images[n_train + n_val:]

    for img in train_imgs:
        shutil.copy(os.path.join(base_dir, cls, img),
                    os.path.join(output_dir, "train", cls, img))

    for img in val_imgs:
        shutil.copy(os.path.join(base_dir, cls, img),
                    os.path.join(output_dir, "val", cls, img))

    for img in test_imgs:
        shutil.copy(os.path.join(base_dir, cls, img),
                    os.path.join(output_dir, "test", cls, img))

print("Dataset split complete!")