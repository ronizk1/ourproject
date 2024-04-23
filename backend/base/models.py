from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10)  # 'admin' or 'user'
    type = models.CharField(max_length=10)  # 'customer' or 'seller'

    def __str__(self):
        return f"{self.user.username}'s profile"

class CustomerProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    image = models.ImageField( null=True, blank=True, default='placeholder.png')

    def __str__(self):
        return f"{self.user_profile.user.username}'s customer profile"

class SellerProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    image = models.ImageField( null=True, blank=True, default='placeholder.png')
    years_of_experience = models.IntegerField()
    bio = models.TextField()
    address = models.TextField()

    def __str__(self):
        return f"{self.user_profile.user.username}'s seller profile"

class Service(models.Model):
    kind = models.TextField() 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField()

    def __str__(self):
        return self.kind

class PicsPosts(models.Model):
    service_type = models.TextField() 
    image = models.ImageField( null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.description

class Appointment(models.Model):
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    type_of_service = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    approved = models.CharField(max_length=10)  # 'true', 'false', 'pending'

    def __str__(self):
        return f"{self.customer.user_profile.user.username} - {self.seller.user_profile.user.username} - {self.type_of_service.kind}"

class NextAppointment(models.Model):
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
    type_of_service = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    approved = models.CharField(max_length=10)  # 'true', 'false', 'pending'

    def __str__(self):
        return f"{self.customer.user_profile.user.username} - {self.seller.user_profile.user.username} - {self.type_of_service.kind}"
