import tensorflow as tf
import numpy as np


class Utils():

    def __init__(self,path_model:str,
                 path:str,
                 label_dic:str):
        
        self.path_model = path_model
        self.path = path
        self.label_dic = label_dic
    
    def load_model(self):
        return tf.keras.models.load_model(self.path_model)

    def load_img(self):
        img=tf.keras.utils.load_img(self.path,target_size = (256,256))
        img=tf.keras.utils.img_to_array(img) / 255.0
        img = np.expand_dims(img,axis = 0)
    
        return img

    def predict(self):
        model = self.load_model()
        img = self.load_img()
        prediction = model.predict(img)
        y_pred = np.argmax(prediction)
        return self.label_dic[y_pred]






if __name__ =='__main__':
        
        label_dict = {0: 'Avulsion fracture', 1: 'Comminuted fracture', 2: 'Fracture Dislocation', 3: 'Greenstick fracture', 4: 'Hairline Fracture', 5: 'Impacted fracture', 6: 'Longitudinal fracture', 7: 'Oblique fracture', 8: 'Pathological fracture', 9: 'Spiral Fracture'}
        PATH = r'./model/cnn_last_try.keras'
        IMG_PATH = r'./image_test\Avulsion fracture/Test/1-s2-0-S0899707114002836-gr2_jpg.rf.bb8ed4dee892edbb760f6ce687d74ba5.jpg'
        ut = Utils(PATH,IMG_PATH,label_dict)
        prediction = ut.predict()
        print(prediction)
       
        
        

