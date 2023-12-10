import json
import pickle
import numpy as np
import statistics
import pandas as pd


__disease_drug = None
__symptoms = None
__model = None
__disease=None
df=pd.read_csv(r"C:\Users\srini\OneDrive\Desktop\disease2drug\dataset\Training.csv")
prognosis_mapping = {category: index for index, category in enumerate(df['prognosis'].unique())}


df['prognosis_numeric'] = df['prognosis'].map(prognosis_mapping)
df2=pd.read_csv(r"C:\Users\srini\OneDrive\Desktop\disease2drug\dataset\Drug.csv")
Drug_numeric={category:index for index,category in enumerate(df2['Drug'].unique())}
df2['Drug_numeric']=df2['Drug'].map(Drug_numeric)
df2['Gender'].replace({'Male':0,'Female':1},inplace=True)
Disease_numeric={ct:index for index,ct in enumerate(df2['Disease'].unique())}
df2['Disease_numeric']=df2['Disease'].map(Disease_numeric)


# For all matched specific disease sympotms in general put 1 and unmatched put 0
# For all matched specific disease sympotms in general put 1 and unmatched put 0
def predict(input):
    # Initialize a list to store symptom binary values
    list_c = [0] * len(__symptoms)
    global __disease_drug
    # Check if each symptom in input matches with the symptoms list
    for z in range(len(__symptoms)):
        for k in input:
            if k == __symptoms[z]:
                list_c[z] = 1

    # Convert the list to a NumPy array
    test = np.array(list_c)

    # Reshape the array to have a single row
    test = test.reshape(1, -1)
    result = []
    # for model in __model:
    #     result.append(model.predict(test)[0])
    result.append(__model[1].predict(test)[0])
    result.append(__model[2].predict(test)[0])
    result.append(__model[3].predict(test)[0])
    result.append(__model[4].predict(test)[0])
    __disease_drug= df.prognosis[statistics.mode(result)]
    return __disease_drug





# list_b = ['mood_swings', 'spotting_ urination']
# print(predict_disease(list_b, 1, 24))
def get_symptoms_names():
    load_saved_symptoms()
    return __symptoms


def load_saved_symptoms():
    print("loading symptoms.....start")
    #global __drug
    global __symptoms
    global __model
    global __disease
    with open(r"C:\Users\srini\OneDrive\Desktop\disease2drug\symp.json", 'r') as f:
        __symptoms = json.load(f)['colunms_data']
        #print(__columns)
        #__location = __columns[4:]
    # with open(r"C:\Users\srini\OneDrive\Desktop\disease2drug\disease_drug.json", 'r') as f:
    #     __drug = json.load(f)['colunms_data']
    with open(r"C:\Users\srini\OneDrive\Desktop\disease2drug\disease.json", 'r') as f:
        __disease = json.load(f)['colunms_data']
    with open(r"C:\Users\srini\OneDrive\Desktop\disease2drug\SDM", 'rb') as f:
        __model = pickle.load(f)

    print("loading of artifacts...is done")

def predict_drug(gender,age):
    print(__disease_drug)
    print(__disease)
    if __disease_drug.lower() in __disease:
        print("helo")
        index = __disease.index(__disease_drug.lower())
        return  df2.Drug[__model[0].predict([[gender, age, index]])]
    else:
        return  'consult doctor'

if __name__ == "__main__":
    get_symptoms_names()
    print(__symptoms)
    # print(__drug)
    print(__disease)
    list_b = ['mood_swings', 'spotting_ urination']
    print(predict(list_b))
    print(predict_drug(1,23))

