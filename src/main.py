import os
import logging
import pandas as pd
import modules.download_dataset as download_dataset
import modules.clean_data as clean_data
import modules.preprocess_data as preprocess_data
import modules.prepare_data as prepare_data
import modules.training_model as training_model

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        dataset_url = 'https://www.kaggle.com/datasets/fatemehmehrparvar/obesity-levels'
        data_destination = '../dataset'
        download_dataset.download_dataset(dataset_url, data_destination)
        logger.info('Dataset downloaded successfully')

        df = pd.read_csv('../dataset/obesity-levels/ObesityDataSet_raw_and_data_sinthetic.csv')
        df_prepared = clean_data.clean_data(df)
        df_preprocessed = preprocess_data.preprocess_data(df_prepared)
        df_prepared = prepare_data.prepare_data(df_preprocessed)
        training_model.training_model(df_prepared)
    except Exception as e:
        logger.error(f'An error occured: {str(e)}')

if __name__ == "__main__":
    main()