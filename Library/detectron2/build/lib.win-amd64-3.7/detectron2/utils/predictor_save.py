import numpy as np

class PredictorSave:
    def __init__(self):
        self.has = []

    def save_instance_predictions(self, predictions):
        num_instances = len(predictions)
        if num_instances == 0:
            return None

        boxes = predictions.pred_boxes.tensor.numpy() if predictions.has("pred_boxes") else None
        scores = predictions.scores if predictions.has("scores") else None
        classes = predictions.pred_classes.numpy() if predictions.has("pred_classes") else None
        keypoints = predictions.pred_keypoints if predictions.has("pred_keypoints") else None
        masks = predictions.pred_masks if predictions.has("pred_masks") else None

        prediction_output = [num_instances, boxes, scores, classes, keypoints, masks]

        # return num_instances, boxes, scores, classes, keypoints, masks
        return prediction_output

    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return obj