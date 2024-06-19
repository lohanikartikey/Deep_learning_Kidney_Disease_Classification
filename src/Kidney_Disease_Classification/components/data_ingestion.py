import zipfile
import gdown
import os
from Kidney_Disease_Classification import logger
from Kidney_Disease_Classification.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self) -> str:
        '''
        Fetch data from url
        '''
        try:
            url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs(self.config.root_dir, exist_ok=True)
            logger.info(f"Downloading data from {url} into file {zip_download_dir}")

            file_id = url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id, zip_download_dir)
            logger.info(f"Download Successful from {url} into {zip_download_dir}")
        except Exception as e:
            raise e
    
    def unzip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        