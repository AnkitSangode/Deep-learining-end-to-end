from CNN_Classifier.constants import*
from CNN_Classifier.utils.common import read_yaml,create_directories
from CNN_Classifier.entity.config_entity import (DataIngestionConfig,
                                                 PrepareBaseModelConfig,)


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

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
          config = self.config.prepare_base_model

          create_directories([config.root_dir])

          prepare_base_model_config = PrepareBaseModelConfig(
                root_dir= Path(config.root_dir),
                base_model_path= Path(config.base_model_path),
                updated_base_model_path= Path(config.updated_base_model_path),
                params_image_size= self.params.IMAGE_SIZE,
                params_learning_rate = self.params.LEARNING_RATE,
                params_include_top= self.params.INCLUDE_TOP,
                params_weights= self.params.WEIGHTS,
                params_classes= self.params.CLASSES
          )
          return prepare_base_model_config
        