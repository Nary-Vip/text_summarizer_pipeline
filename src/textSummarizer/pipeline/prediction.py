from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, pipeline
    
class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config() # To load the model and tokenizer.
    
    def predict(self, text, maxLength):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)

        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": maxLength}

        pipe = pipeline("summarization", model=self.config.model_path ,tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\n Summary: ")
        print(output)

        return output