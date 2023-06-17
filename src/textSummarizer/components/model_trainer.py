import torch
import os
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
from textSummarizer.entity import TrainerConfig

class ModelTrainer:
    def __init__(self, config: TrainerConfig):
        self.config = config

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using {device} device")
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collector = DataCollatorForSeq2Seq(tokenizer, model=model)

        # Loading the data
        dataset = load_from_disk(self.config.data_path)

        training_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            warmup_steps=self.config.warmup_steps,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=1e6,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
        )


        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=dataset["test"], # Just for skipping the high training time... change it to "train" for actual training
            eval_dataset=dataset["validation"],
            data_collator=seq2seq_data_collector,
            tokenizer=tokenizer,
        )

        trainer.train()

        # Save the model
        model.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        # Save the tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-tokenizer"))
