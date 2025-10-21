import os
import sys
import dill

from src.exception import CustomException
from sklearn.metrics import r2_score


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
		# models is expected to be a dict: {name: estimator}
		for name, model in models.items():
			# train
			model.fit(X_train, y_train)

			# predict
			y_train_pred = model.predict(X_train)
			y_test_pred = model.predict(X_test)

			# evaluate
			train_model_score = r2_score(y_train, y_train_pred)
			test_model_score = r2_score(y_test, y_test_pred)

			report[name] = {
				'train_r2': float(train_model_score),
				'test_r2': float(test_model_score)
			}

		return report
	except Exception as e:
		raise CustomException(e, sys)