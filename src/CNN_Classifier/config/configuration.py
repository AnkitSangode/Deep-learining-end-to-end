from CNN_Classifier.constants import*
from CNN_Classifier.utils.common import read_yaml,create_directories
from CNN_Classifier.entity.config_entity import (DataIngestionConfig,
                                                 PrepareBaseModelConfig,
                                                 PrepareCallbacksConfig,
                                                 TrainingConfig,
                                                 EvaluationConfig)
from pathlib import Path
import os


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
    
    def get_prepare_callback_config(self) -> PrepareCallbacksConfig:
        config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath) 
        create_directories([
            Path(model_ckpt_dir),
            Path(config.tensorboard_root_log_dir)
        ])  

        prepare_callback_config = PrepareCallbacksConfig(
            root_dir= Path(config.root_dir),
            tensorboard_root_log_dir= Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath= Path(config.checkpoint_model_filepath)
        )

        return prepare_callback_config
    
    def get_prepare_callback_config(self) -> PrepareCallbacksConfig:
        config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath) 
        create_directories([
            Path(model_ckpt_dir),
            Path(config.tensorboard_root_log_dir)
        ])  

        prepare_callback_config = PrepareCallbacksConfig(
            root_dir= Path(config.root_dir),
            tensorboard_root_log_dir= Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath= Path(config.checkpoint_model_filepath)
        )

        return prepare_callback_config
    
    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir,'Chicken-fecal-images')
        create_directories([
            Path(training.root_dir)
        ])

        training_config = TrainingConfig(
            root_dir= Path(training.root_dir),
            trained_model_path= Path(training.trained_model_path),
            updated_base_model_path= Path(prepare_base_model.updated_base_model_path),
            training_data= Path(training_data),
            params_epochs= params.EPOCHS,
            params_batch_size= params.BATCH_SIZE,
            params_is_augmentation= params.AUGMENTATION,
            params_image_size= params.IMAGE_SIZE

        )

        return training_config
    
    def get_evaluation_config(self):
        eval_config = EvaluationConfig(
        path_of_model= Path("artifacts/training/trained_model.keras"),
        training_data= Path("artifacts/data_ingestion/Chicken-fecal-images"),
        all_params= self.params,
        params_image_size= self.params.IMAGE_SIZE,
        params_batch_size= self.params.BATCH_SIZE
    )

        return eval_config
        