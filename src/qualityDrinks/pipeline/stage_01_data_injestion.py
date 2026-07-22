from qualityDrinks.config.configuration import ConfigurationManager
from qualityDrinks.components.data_injestion import DataInjestion
from qualityDrinks import logger


STAGE_NAME = "Data Ingestion Stage"

class DataInjestionTrainingPipeline:
    def __init__(self):
        pass    
    def main(self):
        config = ConfigurationManager()
        data_injestion_config = config.get_data_injestion_config()
        data_injestion = DataInjestion(config=data_injestion_config)
        data_injestion.download_file()
        data_injestion.extract_zip_file()
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataInjestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed!<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e