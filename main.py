from networksecurity2.components.data_ingestion import DataIngestion
from networksecurity2.components.data_validation import DataValidation
from networksecurity2.exception.exception import NetworkSecurityException
from networksecurity2.logging.logger import logging
from networksecurity2.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity2.entity.config_entity import TrainingPipelineConfig

import sys

if __name__=='__main__':
    try:
        trainingpipelinfconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelinfconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
        data_validation_config = DataValidationConfig(trainingpipelinfconfig)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("data Validation completed")
        print(data_validation_artifact)


    except Exception as e:
           raise NetworkSecurityException(e,sys)