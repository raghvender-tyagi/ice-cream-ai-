
from django.contrib import admin
from .models import IceCream 
from   .models import User

# Register the model
admin.site.register(IceCream)
admin.site.register(User)