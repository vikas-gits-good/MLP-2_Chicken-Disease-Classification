from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from src.cnnClassifier.pipeline.stage_02_prep_base_model import (
    PrepareBaseModelTrainingPipeline,
)

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Started: {STAGE_NAME} <<<<<<")
    data_ings = DataIngestionTrainingPipeline()
    data_ings.main()
    logger.info(f">>>>>> Finished: {STAGE_NAME} <<<<<<\nx=========================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"
try:
    logger.info("*************************")
    logger.info(f">>>>>> Started: {STAGE_NAME} <<<<<<")

    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Finished: {STAGE_NAME} <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
