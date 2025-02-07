from django.db import models
from django.contrib.auth.models import User

class House(models.Model):
    CATEGORY_CHOICES = [
        ('bedsitter', 'Bedsitter'),
        ('single_bedroom', 'Single Bedroom'),
        ('two_bedroom', 'Two Bedroom'),
    ]
    name = models.CharField(max_length=100, default="Not Provided")  # New field for the house name
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='house_images/')
    is_booked = models.BooleanField(default=False)
   
    def __str__(self):
        return f"{self.name} - {self.get_category_display()} - {self.description[:20]}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    room_no = models.CharField(max_length=10, default="Not Provided")  # Default value added
    contact = models.CharField(max_length=15, default="Not Provided")  # Default value added

    def __str__(self):
        return f"{self.user.username} - {self.house} - Room {self.room_no}"



# Removed duplicate Booking class definition


class HouseImage(models.Model):
    house = models.ForeignKey(House, related_name='additional_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='houses/additional_images/')

class Complaint(models.Model):
    name = models.CharField(max_length=100)  # Customer name
    contact = models.CharField(max_length=15)  # Customer contact
    room_number = models.CharField(max_length=10)  # Room number
    message = models.TextField()  # Complaint message
    image = models.ImageField(upload_to='complaint_images/', blank=True, null=True)  # Optional image
    video = models.FileField(upload_to='complaint_videos/', blank=True, null=True)  # Optional video (e.g., MP4)
    response = models.TextField(blank=True, null=True)  # Admin response
    date_submitted = models.DateTimeField(auto_now_add=True)  # Submission date
    date_responded = models.DateTimeField(blank=True, null=True)  # Response date (set when admin responds)

    def __str__(self):
        return f"Complaint from {self.name} - Room {self.room_number}"


class PaymentRecord(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
    ]

    name = models.CharField(max_length=100)
    room_no = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)
    receipt = models.ImageField(upload_to='receipts/')
    date_submitted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    amount_received = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # New field

    def __str__(self):
        return f"{self.name} - {self.room_no}"

    class Meta:
        verbose_name = "Payment Record"
        verbose_name_plural = "Payment Records"



class invoice(models.Model):
     booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="invoices")
     water_bill = models.DecimalField(max_digits=10, decimal_places=2)
     rent = models.DecimalField(max_digits=10, decimal_places=2)
     garbage_fee = models.DecimalField(max_digits=10, decimal_places=2)
     date_posted = models.DateTimeField(auto_now_add=True)
     is_approved = models.BooleanField(default=False)

     def __str__(self):
         return f"Invoice for {self.booking.user.username} - {self.booking.house.category}"

