from django.apps import AppConfig



class RecsysConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recsys'
    
    def ready(self):
        from recsys.services import RecSysModel, RecSysService
        # train model
        RecSysService.export_rating_to_csv()
        RecSysService.export_view_to_csv()

        model = RecSysModel.instance()
        model.train()
