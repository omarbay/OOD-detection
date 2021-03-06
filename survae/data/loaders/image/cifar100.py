from survae.data.datasets.image import UnsupervisedCIFAR100
from torchvision.transforms import Compose, ToTensor
from survae.data.transforms import Quantize
from survae.data import TrainTestLoader, DATA_PATH


class CIFAR100(TrainTestLoader):
    '''
    The CIFAR100 dataset of (Krizhevsky & Hinton, 2009):
    https://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf
    '''

    def __init__(self, root=DATA_PATH, download=True, num_bits=8,
                 pil_transforms=[]):

        self.root = root

        # Define transformations
        trans_train = pil_transforms + [ToTensor()]  # , Quantize(num_bits)]
        trans_test = [ToTensor()]  # , Quantize(num_bits)]

        # Load data
        self.train = UnsupervisedCIFAR100(
            root, train=True, transform=Compose(trans_train),
            download=download)
        self.test = UnsupervisedCIFAR100(
            root, train=False, transform=Compose(trans_test))
