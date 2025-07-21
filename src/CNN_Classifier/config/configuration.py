from CNN_Classifier.constants import*
from CNN_Classifier.utils.common import read_yaml,create_directories
from CNN_Classifier.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(
        self,
        cofig_file_path = CONFIG_FILE_PATH,
        params_file_path = PARAMS_FILE_PATH):
        
        self.config = read_yaml(cofig_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_url= config.source_url,
            local_data_path= config.local_data_path,
            unzip_dir= config.unzip_dir
        ) 
        return data_ingestion_config