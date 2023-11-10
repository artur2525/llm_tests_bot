from datasets import load_dataset
import random

class poem:

    def __init__(self):
        self.random_numb = random.randint(0, 100)
        self.dataset = []

    def download_dataset(self):
        self.dataset = load_dataset('IlyaGusev/stihi_ru', streaming=True, split = 'train')

    def random_poem(self):
        if self.dataset == []:
            self.download_dataset()
        return str(next(iter(self.dataset.shuffle(self.random_numb).take(1)))['text'])
