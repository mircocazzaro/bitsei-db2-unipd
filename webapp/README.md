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
Install the dependencies using Yarn (preferred) or NPM.
`yarn install` or `npm install --save`

Run the application on port `1234`, run this command in the project directory.
`yarn run dev` or `npm run dev`
