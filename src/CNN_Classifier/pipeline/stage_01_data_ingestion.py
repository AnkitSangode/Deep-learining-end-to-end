from CNN_Classifier.config.configuration import ConfigurationManager
from CNN_Classifier.components.data_ingestion import DataIngestion
from CNN_Classifier import logger


STAGE_NAME = 'Data Ingestion Stage'

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()       # ✅ First download the ZIP
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<< \n\nx==============x")
    except Exception as e:
        logger.exception(e)
