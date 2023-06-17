from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTranformation

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        transformation_config = config.get_transformation_config()
        data_transformation = DataTranformation(transformation_config)
        data_transformation.convert()