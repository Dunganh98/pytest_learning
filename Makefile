install:
		pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
		python -m pytest -vv --cov=wikiphrases test_wikiphrases.py --cov=NLPLogic test_simpleNLP.py

format:
		black *.py NLPLogic

lint:
		pylint --disable=R,C *.py NLPLogic/*.py

all: install lint test format