from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)


STAGE_NAME = "Data Ingestion Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Started: {STAGE_NAME} <<<<<<")
        data_ings = DataIngestionTrainingPipeline()
        data_ings.main()
        logger.info(
            f">>>>>> Finished: {STAGE_NAME} <<<<<<\nx=========================x"
        )
    except Exception as e:
        logger.exception(e)
        raise e
