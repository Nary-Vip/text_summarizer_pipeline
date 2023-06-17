from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline

STAGE_NAME = "Data  Ingestion stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed! <<<<")

    STAGE_NAME = "Data Validation stage"
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed! <<<<")

    STAGE_NAME = "Data Transformation stage"
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed! <<<<")


except Exception as e:
    logger.exception(e)
    raise e