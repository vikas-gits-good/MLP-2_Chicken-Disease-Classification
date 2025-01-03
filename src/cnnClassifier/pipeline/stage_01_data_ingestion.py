from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.data_ingestion import DataIngestion
from src.cnnClassifier import logger


STAGE_NAME = "Data Ingestion Stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ings_config = config.get_data_ings_config()
        data_ings = DataIngestion(config=data_ings_config)
        data_ings.download_file()
        data_ings.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Started: {STAGE_NAME} <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Finished: {STAGE_NAME} <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
