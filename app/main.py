from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sodapy import Socrata
from typing import Dict

app = FastAPI()

client = Socrata("data.wa.gov", None)

class VehicleStats(BaseModel):
    vehicle_count: int
    average_electric_range: float

@app.get("/vehicle_stats/{model_year}", response_model=Dict[str, VehicleStats])
def vehicle_stats(model_year: int):
    try:
        soql_query = f"""
            SELECT make, COUNT(*) as vehicle_count, AVG(electric_range) as avg_electric_range
            WHERE model_year = '{model_year}'
            GROUP BY make
        """
        results = client.get("f6w7-q2d2", query=soql_query)
        
        if not results:
            raise HTTPException(status_code=404, detail="No data found for the specified model year")

        aggregated_vehicle_stats = {
            result["make"]: VehicleStats(
                vehicle_count=int(result["vehicle_count"]),
                average_electric_range=float(result["avg_electric_range"])
            )
            for result in results
        }

        return aggregated_vehicle_stats

    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching data: " + str(e))

