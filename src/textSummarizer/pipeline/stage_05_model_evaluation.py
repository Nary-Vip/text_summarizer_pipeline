from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        trainer_config = config.get_model_evaluation_config()
        training_model = ModelEvaluation(trainer_config)
        training_model.evaluate()