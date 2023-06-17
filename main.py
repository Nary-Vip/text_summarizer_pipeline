from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

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

    STAGE_NAME = "Model Training stage"
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_transformation = ModelTrainerPipeline()
    data_transformation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed! <<<<")


    STAGE_NAME = "Model Evalutaion stage"
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_transformation = ModelEvaluationPipeline()
    data_transformation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed! <<<<")


except Exception as e:
    logger.exception(e)
    raise e