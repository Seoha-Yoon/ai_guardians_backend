import cv2

from guardians_of_children.preprocessing.extract_audio import extract
from guardians_of_children.violence_predictor.qualitativeAnalysis_custom import calculate
from guardians_of_children.audio_classification.SVC import classify

def run():

    # 음원 추출 후 저장
    extract()

    # 폭력 동작 감지 (확률)
    number = calculate()
    res = classify()

    return number, res