import os
import boto3
import time
from botocore.vendored import requests
from websock.web import websocket
import os
from dotenv import load_dotenv


load_dotenv()


class TrainBikeModel:

    INSTANCE = os.getenv('INSTANCE')

    def __init__(self):
        self.client = boto3.client('sagemaker')
        self.client
        self.url = self.client.create_presigned_notebook_instance_url(NotebookInstanceName=self.INSTANCE)['AuthorizedUrl']
        self.url_tokens = self.url.split('/')

    def execute(self):
        http_proto = self.url_tokens[0]
        http_hn = self.url_tokens[2].split('?')[0].split('#')[0]
        s = requests.Session()
        r = s.get(self.url)
        cookies = "; ".join(key + "=" + value for key, value in s.cookies.items())
        ws = websocket.create_connection("wss://{}/terminals/websocket/1".format(http_hn),
                                         cookie=cookies,host=http_hn,origin=http_proto + "//" + http_hn)
        ws.send("""[ "stdin", "jupyter nbconvert --execute --to notebook --inplace /home/ec2-user/SageMaker/model.ipynb --ExecutePreprocessor.kernel_name=python3 --ExecutePreprocessor.timeout=1500\\r" ]""")
        time.sleep(1)
        ws.close()
        return None