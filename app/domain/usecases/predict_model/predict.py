from app.domain.models.data_predict_model import RequestPredictModel, ResponsePredictModel
import boto3
import tensorflow as tf
from sklearn.feature_extraction import DictVectorizer
from dotenv import load_dotenv
import pickle
from botocore.config import Config
import os


load_dotenv()



class BikeModel:

    PATH_MODEL = os.getenv('PATH_MODEL')
    PATH_VEC = os.getenv('PATH_VEC')
    BUCKET_NAME = os.getenv('BUCKET_NAME')

    def __init__(self, request_data: RequestPredictModel):
        load_dotenv()
        self.client = boto3.client("s3",
                                   config=Config(s3={'addressing_style': 'path'}))
        self.request_data = request_data
        self.model = self.load_model()
        self.vec = self.load_vec()

    def load_model(self) -> tf.keras.Model:
        self.client.download_file(self.BUCKET_NAME,self.PATH_MODEL, 'model.h5')
        return tf.keras.models.load_model('model.h5')

    def load_vec(self) -> DictVectorizer:
        self.client.download_file(self.BUCKET_NAME,self.PATH_VEC, 'vect.pkl')
        return pickle.load(open('vect.pkl', 'rb'))

    def predict(self):
        data = self.vec.transform(self.request_data.dict())
        return ResponsePredictModel(bike_number=self.model.predict(data)[0][0])

