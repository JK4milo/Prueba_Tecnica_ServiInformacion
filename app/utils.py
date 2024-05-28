import tensorflow as tf
import numpy as np


class Utils():
    """Utils class that perform the call an predict to the model

        Args:

            None

        Returns:

            None
    """

    def __init__(self, path_model: str,
                 path: str,
                 label_dic: str):
        """Init Constructor.

        Args:

            path_model(str): Receive path_model, can alternate between the 2 possible models.
            path:(str): Receive image path.
            label_dic(dict): Diccionary with the labels

        Returns:

            None
        """
        self.path_model = path_model
        self.path = path
        self.label_dic = label_dic

    def load_model(self):
        """Load the model using tf instance

        Args:

            None

        Returns:

            tf.keras.models.load_model(self.path_model)
        """
        return tf.keras.models.load_model(self.path_model)

    def load_img(self):
        """Load the image using tf instance

        Args:

            None

        Returns:

            img(np.ndarray): An array with the correct shape to the model.
        """
        img = tf.keras.utils.load_img(self.path, target_size=(256, 256))
        img = tf.keras.utils.img_to_array(img) / 255.0
        img = np.expand_dims(img, axis=0)

        return img

    def predict(self):
        """Classify the label

        Args:

            None

        Returns:

            self.label_dic[y_pred](str): Classification done by the model.
        """
        model = self.load_model()
        img = self.load_img()
        prediction = model.predict(img)
        y_pred = np.argmax(prediction)
        return self.label_dic[y_pred]


if __name__ == '__main__':

    label_dict = {0: 'Avulsion fracture', 1: 'Comminuted fracture', 2: 'Fracture Dislocation', 3: 'Greenstick fracture', 4: 'Hairline Fracture',
                  5: 'Impacted fracture', 6: 'Longitudinal fracture', 7: 'Oblique fracture', 8: 'Pathological fracture', 9: 'Spiral Fracture'}
    PATH = r'./model/cnn_last_try.keras'
    IMG_PATH = r'./image_test\Avulsion fracture/Test/1-s2-0-S0899707114002836-gr2_jpg.rf.bb8ed4dee892edbb760f6ce687d74ba5.jpg'
    ut = Utils(PATH, IMG_PATH, label_dict)
    prediction = ut.predict()
    print(prediction)
