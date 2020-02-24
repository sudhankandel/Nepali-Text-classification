import pickle
loaded_model = pickle.load(open('models/finalized_model.sav', 'rb'))
load_vectorized = pickle.load(open('models/vectorized_model.sav', 'rb'))
def SVM_Predict(text):
    text=[text]
    predict_data=load_vectorized.transform(text)
    category=loaded_model.predict(predict_data)
    return category
