import os
import urllib.request as request
import zipfile
from CNN_Classifier import logger
from CNN_Classifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_path):
            filename,header = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_path
            )
            logger.info(f"Looking for ZIP file at: {self.config.local_data_path}")
            logger.info(f"{filename} download! with following info: \n{header}")
        else:
            logger.info(f"File already exists")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_path,'r') as zip_ref:
            zip_ref.extractall(unzip_path)

    