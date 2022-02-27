from django.contrib import admin
from .models import customer, customer_notes, dog, dog_breeds, announcement

# Register your models here.
admin.site.register(customer)
admin.site.register(customer_notes)
admin.site.register(dog)
admin.site.register(dog_breeds)
admin.site.register(announcement)
