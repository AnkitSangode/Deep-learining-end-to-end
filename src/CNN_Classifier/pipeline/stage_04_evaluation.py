from CNN_Classifier.config.configuration import ConfigurationManager
from CNN_Classifier.components.evaluation import Evaluation
from CNN_Classifier import logger

STAGE_NAME = "Evaluation stage"

class EvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        val_config = config.get_evaluation_config()
        evaluation= Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == "__main__":
    try:
        logger.info(f"************")
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f"<<<<<<<<<< stage {STAGE_NAME} completed")
    except Exception as e:
        raise e