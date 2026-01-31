from networksecurity2.components.data_ingestion import DataIngestion
from networksecurity2.exception.exception import NetworkSecurityException
from networksecurity2.logging.logger import logging
from networksecurity2.entity.config_entity import DataIngestionConfig
from networksecurity2.entity.config_entity import TrainingPipelineConfig

import sys

if __name__=='__main__':
    try:
        trainingpipelinfcongig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelinfcongig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)


    except Exception as e:
           raise NetworkSecurityException(e,sys)