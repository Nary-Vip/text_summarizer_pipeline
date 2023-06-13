from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.logging import logger
from textSummarizer.components.data_ingestion import DataIngestion 

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
        # self.config_manager = ConfigurationManager()
        # self.config = self.config_manager.get_data_ingestion_config()
        # self.data_ingestion = DataIngestion(self.config.data_ingestion)

    def main(self):
        config_mgr = ConfigurationManager()
        data_ingestion_config = config_mgr.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_file()
