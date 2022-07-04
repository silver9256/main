from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([User, Parts, Build, Processor_dropdown, 
	Motherboard_dropdown, Storage_dropdown, Ram_dropdown,
	Graphics_dropdown, Powersupply_dropdown, Chassis_dropdown,
	Fan_dropdown])