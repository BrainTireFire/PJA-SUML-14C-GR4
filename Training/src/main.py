"""
    Ten moduł jest glownym modułem aplikacji.
"""

import logging
import pandas as pd
from modules.data_processing import download_dataset
from modules.data_processing import clean_data
from modules.data_processing import preprocess_data
from modules.data_processing import prepare_data
from modules.data_science import training_model
from modules.data_processing import split_data
from modules.data_science import evaluate_model
from modules.data_science import show_model_data
from modules.data_science import save_model

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """
    Ten moduł jest glownym modułem aplikacji.
    """
    try:
        # dataset_url = 'https://www.kaggle.com/datasets/fatemehmehrparvar/obesity-levels'
        # data_destination = '../dataset'
        # download_dataset.download_dataset(dataset_url, data_destination)
        # logger.info('Dataset downloaded successfully')

        df = pd.read_csv('dataset/obesity-levels/ObesityDataSet_raw_and_data_sinthetic.csv')
        logger.info('Dataset loaded successfully')

        df_prepared = clean_data.clean_data(df)
        logger.info('Dataset cleaned successfully')

        df_preprocessed = preprocess_data.preprocess_data(df_prepared)
        logger.info('Dataset preprocessed successfully')

        df_prepared = prepare_data.prepare_data(df_preprocessed)
        logger.info('Dataset prepared successfully')

        x_train, x_test, y_train, y_test = split_data.split_data(df_preprocessed)
        logger.info('Dataset splitted successfully')

        model = training_model.training_model(x_train, y_train)
        logger.info('Model trained successfully')

        predictions = evaluate_model.evaluate_model(model, x_test)
        logger.info('Model evaluated successfully')

        show_model_data.show_model_data(y_test, predictions)
        logger.info('Model data shown successfully')

        output_dir = 'models'
        save_model.save_model(model, output_dir)
        logger.info('Model saved successfully')

    except Exception as e:
        logger.error(f'An unexpected error occurred: {str(e)}')

if __name__ == "__main__":
    main()
