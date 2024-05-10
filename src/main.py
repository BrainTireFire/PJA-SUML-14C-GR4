import os
import logging
import pandas as pd
import modules.data_processing.download_dataset as download_dataset
import modules.data_processing.clean_data as clean_data
import modules.data_processing.preprocess_data as preprocess_data
import modules.data_processing.prepare_data as prepare_data
import modules.data_science.training_model as training_model
import modules.data_processing.split_data as split_data
import modules.data_science.evaluate_model as evaluate_model
import modules.data_science.show_model_data as show_model_data
import modules.data_science.save_model as save_model

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        dataset_url = 'https://www.kaggle.com/datasets/fatemehmehrparvar/obesity-levels'
        data_destination = '../dataset'
        download_dataset.download_dataset(dataset_url, data_destination)
        logger.info('Dataset downloaded successfully')

        df = pd.read_csv('../dataset/obesity-levels/ObesityDataSet_raw_and_data_sinthetic.csv')
        logger.info('Dataset loaded successfully')

        df_prepared = clean_data.clean_data(df)
        logger.info('Dataset cleaned successfully')

        df_preprocessed = preprocess_data.preprocess_data(df_prepared)
        logger.info('Dataset preprocessed successfully')

        df_prepared = prepare_data.prepare_data(df_preprocessed)
        logger.info('Dataset prepared successfully')

        X_train, X_test, y_train, y_test = split_data.split_data(df_preprocessed)
        logger.info('Dataset splitted successfully')

        model = training_model.training_model(X_train, y_train)
        logger.info('Model trained successfully')

        predictions = evaluate_model.evaluate_model(model, X_test)
        logger.info('Model evaluated successfully')    
        
        show_model_data.show_model_data(model, y_test, predictions)
        logger.info('Model data shown successfully')

        output_dir = 'models'
        save_model.save_model(model, output_dir)
        logger.info('Model saved successfully')

    except Exception as e:
        logger.error(f'An error occured: {str(e)}')

if __name__ == "__main__":
    main()