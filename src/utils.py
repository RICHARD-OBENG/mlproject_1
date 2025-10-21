import os
import sys
import dill

from src.exception import CustomException


def save_object(file_path, obj):
	"""Serialize `obj` to `file_path` using dill, creating parent dirs as needed."""
	try:
		dir_path = os.path.dirname(file_path)
		if dir_path and not os.path.exists(dir_path):
			os.makedirs(dir_path, exist_ok=True)

		with open(file_path, 'wb') as f:
			dill.dump(obj, f)
	except Exception as e:
		raise CustomException(e, sys)


def load_object(file_path):
	"""Load and return a Python object serialized with dill from `file_path`."""
	try:
		with open(file_path, 'rb') as f:
			return dill.load(f)
	except Exception as e:
		raise CustomException(e, sys)

def evaluate_models(X_train,X_test,y_train,y_test,models):
	try:
		report = {}
		for i in range(len(list(models))):
			model = list(models.values())[i]
			
            model.fit(X_train,y_train)


            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train,y_train_pred)

            train_model_score = r2_score(y_test,y_test_pred)
	
            report[list(models.keys())[i]] = test_model_score
        return report
    except Exception as e:
        raise CustomException(e,sys)