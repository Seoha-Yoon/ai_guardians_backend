from guardians_of_children.violence_predictor.qualitativeAnalysis_custom import calculate
from guardians_of_children.audio_classification.SVC import classify

def run():
    number = calculate()
    res = classify()
    return number, res