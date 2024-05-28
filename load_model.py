import tensorflow as tf
import numpy as np


def load_model(path):
    return tf.keras.models.load_model(path)

def load_img(path_img):
    img=tf.keras.utils.load_img(path_img,target_size = (256,256))
    img=tf.keras.utils.img_to_array(img) / 255.0
    img = np.expand_dims(img,axis = 0)
    print(img.shape)

    return img

def predict(model,img,dict_):
    prediction = model.predict(img)
    y_pred = np.argmax(prediction)
    return f'the prediction is {dict_[y_pred]}'



if __name__ =='__main__':
    label_dict = {0: 'Avulsion fracture', 1: 'Comminuted fracture', 2: 'Fracture Dislocation', 3: 'Greenstick fracture', 4: 'Hairline Fracture', 5: 'Impacted fracture', 6: 'Longitudinal fracture', 7: 'Oblique fracture', 8: 'Pathological fracture', 9: 'Spiral Fracture'}
    PATH = r'./model/BestCNNModel.keras'
    IMG_PATH = r'./image_test\Avulsion fracture/Test/1-s2-0-S0899707114002836-gr2_jpg.rf.bb8ed4dee892edbb760f6ce687d74ba5.jpg'
    model = load_model(PATH)
    img = load_img(IMG_PATH)
    print(predict(model,img,label_dict))
    
    

