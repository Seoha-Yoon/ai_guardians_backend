import cv2

from guardians_of_children.violence_predictor.qualitativeAnalysis_custom import calculate
from guardians_of_children.audio_classification.SVC import classify

def run(save_dir):
    number, frame = calculate()
    res = classify()

    cv2.imwrite(
        save_dir,
        frame,
    )

    return number, res