from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig

class ConfigurationManager:
    def __init__(self, config_path=CONFIG_FILE_PATH, params_path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
 
        create_directories([self.config.artifacts_root]) 

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config["data_ingestion"]

        create_directories([config["root_dir"]])
        
        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
    
    def get_data_validation(self) -> DataValidationConfig:
        config = self.config["data_validation"]

        create_directories([config.root_dir])
        
        return DataValidationConfig(
            root_dir=Path(config.root_dir),
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )
    

    def get_transformation_config(self) -> DataTransformationConfig:
        config = self.config["data_transformation"]

        create_directories([config.root_dir])

        return DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name
        )