from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_trainer import ModelTrainer

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        trainer_config = config.get_model_trainer_config()
        training_model = ModelTrainer(trainer_config)
        training_model.train()