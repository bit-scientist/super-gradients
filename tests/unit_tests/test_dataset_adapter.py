import unittest
import random
import numpy as np
from typing import List, Tuple

import torch

# from super_gradients.training.utils.detection_utils import DetectionCollateFN
from super_gradients.training.transforms.transforms import pad_targets


def _generate_image_sample() -> np.ndarray:
    return np.array([np.random.random((3, 64, 64))])


def _generate_target_sample() -> Tuple[List, List]:
    n_cls = 10
    n_target = random.randint(3, 10)

    bboxes = [(random.randint(0, 32), random.randint(0, 32), random.randint(32, 64), random.randint(32, 64)) for _ in range(n_target)]
    cls_ids = [random.randint(0, n_cls) for _ in range(n_target)]
    return bboxes, cls_ids


class DictDataset(torch.utils.data.Dataset):
    """Dummy Dataset that returns a few fields grouped as a dict"""

    def __len__(self):
        return 10

    def __getitem__(self, item):
        image = _generate_image_sample()
        bboxes, cls_ids = _generate_target_sample()
        return {"img": image, "bboxes": bboxes, "cls_ids": cls_ids, "index": item}


def dict_dataset_adapter_function(original_item: dict):
    img = original_item["img"]
    target = np.array([[cls_id, *bbox] for cls_id, bbox in zip(original_item["cls_ids"], original_item["bboxes"])])
    return img, pad_targets(targets=target, max_targets=10)


class DatasetAdaptor(torch.utils.data.Dataset):
    """

    :param adapter_function: Converts the Dataset output into a format that is compatible with the collate function.

    """

    def __init__(self, dataset, adapter_function):
        self._dataset = dataset
        self.adapter_function = adapter_function

    def __getitem__(self, index):
        item = self._dataset[index]
        return self.adapter_function(item)

    def __getattr__(self, item):
        getattr(self._dataset, item)


class TestAutoAugment(unittest.TestCase):
    def setUp(self):
        dict_dataset = DictDataset()
        self.dict_dataset_wrapper = DatasetAdaptor(dataset=dict_dataset, adapter_function=dict_dataset_adapter_function)

    def test_adaptor_output(self):
        for item in iter(self.dict_dataset_wrapper):
            self.assertIsInstance(item, tuple, "The dataset wrapper needs to return a tuple")
            self.assertGreaterEqual(len(item), 2, "The dataset needs to be made of at least 2 values (typically image, target)")

    def test_adaptor_dataloader(self):
        from super_gradients.training import dataloaders

        val_dataloader = dataloaders.get(
            dataset=self.dict_dataset_wrapper,
            dataloader_params={"batch_size": 2},
        )
        for img, target in iter(val_dataloader):
            self.assertIsInstance(img, torch.Tensor)
            self.assertIsInstance(target, torch.Tensor)


if __name__ == "__main__":
    unittest.main()
