from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.views import View

# Models for Event, Service, Booking, and others

class Event(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    description = models.TextField()
    services = models.ManyToManyField('Service', related_name='events', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation

    def __str__(self):
        return self.name


class Service(models.Model):
    CATEGORY_CHOICES = [
        ('Venue', 'Venue'),
        ('Catering', 'Catering'),
        ('Decoration', 'Decoration'),
        ('Entertainment', 'Entertainment'),
        ('Photography', 'Photography'),
        ('Other', 'Other'),
    ]

    service_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='services/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')

    def __str__(self):
        return self.service_name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service, related_name='bookings')  # Many-to-many relationship
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.event.name} by {self.user.username}"


class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio_images/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    updated_at = models.DateTimeField(auto_now=True)      # Automatically updates on every save

    def __str__(self):
        return self.title


class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='event_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_gallery/')
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.event.name}"


class Testimonial(models.Model):
    client_name = models.CharField(max_length=200)
    testimonial = models.TextField()
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created

    def __str__(self):
        return self.client_name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the contact is created

    def __str__(self):
        return self.name

class BookServiceView(View):
    def post(self, request, event_id):
        # Get the event for which services are being booked
        event = get_object_or_404(Event, id=event_id)

        # Get the list of selected services from the form
        selected_services = request.POST.getlist('services')  # Fetch service IDs as list
        
        if not selected_services:
            messages.error(request, 'Please select at least one service.')
            return redirect('event_detail', event_id=event.id)  # Redirect if no services are selected
        
        # Create a booking without services initially
        booking = Booking.objects.create(event=event, user=request.user)
        
        # Get the selected service objects
        services = Service.objects.filter(id__in=selected_services)

        # Set the services to the booking using .set()
        booking.services.set(services)

        # Send a confirmation email
        service_names = ", ".join([service.service_name for service in services])
        send_mail(
            subject=f'Booking Confirmation for {event.name}',
            message=f'You have successfully booked the following services for the event "{event.name}": {service_names}.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[request.user.email],
        )

        # Display a success message
        messages.success(request, f'Successfully booked the following services for {event.name}: {service_names}.')
        
        # Redirect back to the event detail page
        return redirect('event_detail', event_id=event.id)