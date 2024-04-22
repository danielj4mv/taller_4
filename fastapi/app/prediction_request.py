from pydantic import BaseModel

class PredictionRequest(BaseModel):

    elevation: int
    aspect: int 
    slope: int 
    horizontal_distance_to_hydrology: int
    vertical_distance_to_hydrology: int 
    horizontal_distance_to_roadways: int
    hillshade_9am: int 
    hillshade_noon: int 
    hillshade_3pm: int 
    horizontal_distance_to_fire_points: int 
    wilderness_area: str
    soil_type: str
    
    
    class Config:
        # definicion de un ejemplo para probar rapidamente el funcionamiento del API
        json_schema_extra = {
            "example": {"elevation": 2848,
                        "aspect": 65,
                        "slope": 20,
                        "horizontal_distance_to_hydrology": 170,
                        "vertical_distance_to_hydrology":23,
                        "horizontal_distance_to_roadways":331,
                        "hillshade_9am":234,
                        "hillshade_noon":195,
                        "hillshade_3pm":84,
                        "horizontal_distance_to_fire_points":295,
                        "wilderness_area":"Commanche",
                        "soil_type": "C7757"
                        }
        }
