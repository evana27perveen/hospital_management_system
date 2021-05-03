from django.contrib import admin
from App_main.models import AdmissionModel, AppointmentModel, TestModel, FeedBackModel, DischargeModel

# Register your models here.£
admin.site.register(AdmissionModel)
admin.site.register(AppointmentModel)
admin.site.register(TestModel)
admin.site.register(DischargeModel)
admin.site.register(FeedBackModel)
