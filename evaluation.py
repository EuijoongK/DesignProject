import numpy as np
from PIL import Image

def calculate_iou(gt_path, pred_path):
    gt_image = Image.open(gt_path)
    new_size = (256, 256)
    gt_image = gt_image.resize(new_size)
    
    gt_image = np.array(gt_image)
    pred_image = np.array(Image.open(pred_path))
    
    assert gt_image.shape == pred_image.shape, "Ground truth and prediction images must have the same shape"

    tp = np.sum((gt_image == 255) & (pred_image != 0))
    fp = np.sum((gt_image == 0) & (pred_image != 0))
    fn = np.sum((gt_image == 255) & (pred_image == 0))

    iou = tp / (tp + fp + fn)
    return iou

# Example usage
gt_path = "/mnt/c/Users/MICS/Desktop/test_gt2/gt_160.png"
pred_path = "/mnt/c/Users/MICS/Desktop/test_prediction_BCE2_35epoch/deform_160.png"

iou_score = calculate_iou(gt_path, pred_path)
print(f"IoU Score: {iou_score}")
