1. Set up a Python environment <br>
 $ python -m venv env <br>
 $ source ./env/bin/activate

2. Install dependencies <br>
 $ pip install -r requirements.txt <br>
 $ source ./env/bin/activate <br>

3. Start the application <br>
 $ uvicorn app.main:app --reload <br> 

Once Uvicorn is running locally, navigate to the following url to test the endpoint: <br>
http://127.0.0.1:8000/docs#/default/vehicle_stats_vehicle_stats__model_year__get


