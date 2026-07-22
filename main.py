from qualityDrinks import logger
from qualityDrinks.pipeline.stage_01_data_injestion import DataInjestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_injestion = DataInjestionTrainingPipeline()
    data_injestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed!<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e