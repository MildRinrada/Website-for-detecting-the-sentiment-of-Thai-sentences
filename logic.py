# Import libraries
import joblib
import pandas as pd
from joblib import dump, load
from attacut import tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


def calculate_result(input_text):
    # ระบุพาธของไฟล์ที่ต้องการเข้าถึงใน Google Drive
    file_path = 'Thai Emotion.xlsx'
    # อ่านไฟล์ Excel เข้าสู่ DataFrame
    df = pd.read_excel(file_path)
    X = df['text']
    y = df['label']  
    
    count_vect = CountVectorizer(tokenizer=tokenize)
    X_count = count_vect.fit_transform(X)
    
    tf_transformer = TfidfTransformer(use_idf=False)
    tf_transformer.fit(X_count)
    X_tf = tf_transformer.transform(X_count)
    
    clf = MultinomialNB()
    clf.fit(X_tf, y)
    
    new_sentence = input_text
    
    # แปลงประโยคให้อยู่ในรูปแบบของเวกเตอร์
    new_sentence_count = count_vect.transform([new_sentence])
    new_sentence_tf = tf_transformer.transform(new_sentence_count)

    # ทำนายความน่าจะเป็นของแต่ละคลาส
    predicted_probabilities = clf.predict_proba(new_sentence_tf)

    label_map = {0: "ความเศร้า", 1: "ความสุข", 2: "ความรัก", 3: "ความโกรธ"}
    
    # หาดัชนีของค่าที่มากที่สุด
    max_index = predicted_probabilities.argmax()

    # หา Label ที่มีความน่าจะเป็นสูงสุด
    predicted_label = clf.classes_[max_index]

    # แมพ Label เป็นข้อความ
    predicted_label_text = label_map[predicted_label]
    
    result = predicted_label_text

    print("Predicted Label:", predicted_label_text)

    return result

