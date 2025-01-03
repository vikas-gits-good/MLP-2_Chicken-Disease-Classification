from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.prep_base_model import PrepareBaseModel
from src.cnnClassifier import logger

STAGE_NAME = "Prepare Base Model"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prep_bm_config = config.get_prep_base_model_config()
        prep_bm = PrepareBaseModel(config=prep_bm_config)
        prep_bm.get_base_model()
        prep_bm.update_base_model()


if __name__ == "__main__":
    try:
        logger.info("*************************")
        logger.info(f">>>>>> Started: {STAGE_NAME} <<<<<<")

        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Finished: {STAGE_NAME} <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
