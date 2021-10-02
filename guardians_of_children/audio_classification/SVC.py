import os.path

import librosa
import numpy as np
import pickle
from sklearn.externals import joblib
from sklearn.svm import SVC

def features_extractor(file_name):
    audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)
    return mfccs_scaled_features

def load_model(pkl_path):
    clf = SVC(C=2.0, gamma=0.001, probability=True)
    clf_from_joblib = joblib.load(pkl_path)
    return clf_from_joblib

def preprocess(audio_path):
    preprocess_audio = features_extractor(audio_path).reshape(1,-1)
    return preprocess_audio

def predict(preprocess_audio):
    clf_from_joblib = load_model(os.path.join(os.getcwd(), 'guardians_of_children/audio_classification/SVC_fight.pkl'))
    prediction = clf_from_joblib.predict(preprocess_audio)
    if prediction[0] == 0.:
        print('non-fight')
        return 0
    elif prediction[0] == 1.:
        print('fight')
        return 1


def classify():
    preprocess_audio = preprocess(os.path.join(os.getcwd(), 'guardians_of_children/audio_classification/fight_audio_214.wav'))
    return predict(preprocess_audio)