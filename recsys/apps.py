from django.apps import AppConfig
from threading import Thread
import threading
import time

class RecsysConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recsys'
    
    def ready(self):
        from recsys.services import RecSysModel, RecSysService
        import schedule

        # train model
        RecSysService.export_rating_to_csv()
        RecSysService.export_view_to_csv()

        model = RecSysModel.instance()

        model.train()
        def train_model():
            print('train model')
            model.train()

        schedule.every().minutes.do(train_model)
        def run_schedule():
            while True:
                schedule.run_pending()
                time.sleep(1)
        threading.Thread(target=run_schedule).start()
