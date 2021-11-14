from background_task import background
from recsys.services import RecSysService

@background(schedule=10)
def retrain_model():
    print("Retrain model")
    RecSysService.export_rating_to_csv()
