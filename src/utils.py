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
