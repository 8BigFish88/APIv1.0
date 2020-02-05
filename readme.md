#install libraries

pip install -r requirements.txt

# running the app

python app.py

#running the tests

pytest .

#running test with coverage

pytest . -v  --cov-report html --cov=app test/ 
