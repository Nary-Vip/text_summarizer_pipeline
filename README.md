# End to End Text Summarization Project

This project focuses on text summarization using a pre-trained transformer model called Pegasus CNN. The model is fine-tuned with the Samsum Summarization datasets to enable well defined text summarization. Pegasus CNN utilizes a special self-supervised pre-training objective called gap-sentences generation (GSG) designed to perform well on summarization-related downstream tasks.

The implementation follows a modular approach, with a well-defined pipeline that includes:

1. **Data Ingestion**: The process of gathering and importing the text data for summarization. Model sources, data paths, and training arguments are handled and imported from YAML files, providing flexibility and ease of configuration.

2. **Data Transformation**: Preprocessing and formatting the data to prepare it for model training.

3. **Data Validation**: Ensuring the quality and correctness of the data used for fine-tuning the model.

4. **Model Training**: Fine-tuning the Pegasus CNN with the Samsum Summarization datasets.

5. **Model Evaluation**: Assessing the performance and effectiveness of the trained model.

The entire process is extensively logged using a logging library to keep track of crucial information and provide insights during development and deployment.

### Workflow

1. Update the config.yaml file.
2. Update params.yaml
3. Update entity.
4. Update configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the app.py
   
### CI/CD Deployment

This project supports continuous integration and continuous deployment (CI/CD) for both model training and using the model for text summarization. The CI/CD setup ensures seamless integration, testing, and deployment processes, making it easier to manage updates and maintain the summarization capabilities efficiently.

Feel free to explore the project code and let me know if you have any questions or feedback, please don't hesitate to open an issue or reach out to me. Happy summarizing!
