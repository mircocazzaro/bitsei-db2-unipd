## Pre-requisites
Install Virtual Environment on your machine.
```bash
pip install virtualenv
```
Create And Activate Virtual Environment, in the project directory.
```bash
virtualenv venv
source venv/bin/activate
```
Install all the dependencies.
```bash
pip install -r requirements.txt
```

## Run the application
Run the application on port 8081, run this command in the project directory.
```bash
uvicorn main:app --reload --port 8081
```

### API Documentation
API documentation is available at http://localhost:8081/docs, you can see the swagger documentation and test the API's.

### Run the Frontend
Go through the frontend directory and just run the `crime.html` file in your browser.
