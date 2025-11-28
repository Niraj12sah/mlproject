from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion 
#from src.mlproject.components.data_ingestion import DataIngestion
import sys

if __name__=="__main__":
  logging.info("the ecexcution started")

  try:
      #data_ingestion_config=DataIngestionConfig()
      data_ingestion=DataIngestion()
      train_path, test_path =  data_ingestion.initiate_data_ingestion()
  except Exception as e:
    logging.info("Custom Exception")
    raise CustomException(e,sys)