# admin.py

from django.contrib import admin
from .models import Event, Service, Testimonial, Contact, EventImage,PortfolioItem

# Registering models
admin.site.register(Event)
admin.site.register(Service)
admin.site.register(PortfolioItem)
admin.site.register(Testimonial)
admin.site.register(Contact)
admin.site.register(EventImage)
