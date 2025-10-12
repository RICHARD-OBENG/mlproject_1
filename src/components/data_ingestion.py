import os
import sys
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# package-friendly imports: prefer relative imports when used as a package,
# fall back to top-level imports when running the module directly for convenience
# Make sure the project's `src` directory is on sys.path so top-level imports work
# when this module is executed directly (before any import attempts below).
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
src_path = os.path.join(project_root, 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

try:
    from ..exception import CustomException
    from ..logger import logging
except Exception:
    # when running this file directly the relative import may fail; fall back
    # to importing the top-level modules (which now should be importable because
    # we've added src/ to sys.path above).
    from exception import CustomException
    from logger import logging


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # build a platform-independent path to the sample notebook data
            data_path = os.path.join('notebook', 'data', 'stud.csv')
            data = pd.read_csv(data_path)
            logging.info('Read the dataset as dataframe')

            # ensure artifacts directory exists
            artifacts_dir = os.path.dirname(self.ingestion_config.train_data_path)
            if artifacts_dir and not os.path.exists(artifacts_dir):
                os.makedirs(artifacts_dir, exist_ok=True)

            # save raw copy
            data.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info('Train test split initiated')
            train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Ingestion of the data is completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            # wrap any exception into your project's CustomException
            raise CustomException(e, sys)


if __name__ == '__main__':
    # when running directly, make sure src/ is on sys.path so top-level imports work
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    src_path = os.path.join(project_root, 'src')
    if src_path not in sys.path:
        sys.path.append(src_path)

    obj = DataIngestion()
    obj.initiate_data_ingestion()