from qualityDrinks import logger
from qualityDrinks.pipeline.stage_01_data_injestion import DataInjestionTrainingPipeline
from qualityDrinks.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from qualityDrinks.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from qualityDrinks.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_injestion = DataInjestionTrainingPipeline()
    data_injestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed!<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_injestion = DataValidationTrainingPipeline()
    data_injestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed!<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
    
    
STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_injestion = DataTransformationTrainingPipeline()
    data_injestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed!<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = " Model Trainer stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_injestion = ModelTrainerTrainingPipeline()
    data_injestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e