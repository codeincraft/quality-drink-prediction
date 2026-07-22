import os
from pathlib import Path
import urllib.request as request
import zipfile
from qualityDrinks import logger
from qualityDrinks.entity.config_entity import DataIngestionConfig
from qualityDrinks.utils.common import get_size


class DataInjestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! with folowing info: \n{headers}")
        else:
            logger.info(f"file already exists of size: {get_size(Path(self.config.local_data_file))}")
            
            
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extract the zip file into the ddata directory
        Function returns None
        """
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)