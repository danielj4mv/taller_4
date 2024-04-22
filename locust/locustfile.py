from locust import HttpUser, task, constant
from pydantic import BaseModel

class CoverType(BaseModel):
    elevation: int =2848
    aspect: int =65
    slope: int = 20
    horizontal_distance_to_hydrology: int = 170
    vertical_distance_to_hydrology: int = 23
    horizontal_distance_to_roadways: int = 331
    hillshade_9am: int = 234
    hillshade_noon: int = 195
    hillshade_3pm: int = 84
    horizontal_distance_to_fire_points: int = 295
    wilderness_area: str = "Commanche"
    soil_type: str = "C7757"


class LoadTest(HttpUser):
    wait_time = constant(1)
    host = "http://inference:8083"

    @task
    def predict(self):
        request_body = {
		"elevation": 2848,
                "aspect": 65,
                "slope": 20,
                "horizontal_distance_to_hydrology": 170,
                "vertical_distance_to_hydrology": 23,
                "horizontal_distance_to_roadways": 331,
                "hillshade_9am": 234,
                "hillshade_noon": 195,
                "hillshade_3pm": 84,
                "horizontal_distance_to_fire_points": 295,
                "wilderness_area": "Commanche",
                "soil_type": "C7757"
            }
        headers = {
            "Content-Type": "application/json",
        }
        self.client.post(
            "/predict", json=request_body, headers=headers
        )
