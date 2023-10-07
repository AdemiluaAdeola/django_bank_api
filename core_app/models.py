from django.db import models
from auth_app.models import User
from django_countries import Countries

# Create your models here.
class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    phone = models.IntegerField()
    sex = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female')))
    date= models.DateField(auto_now_add=True,null=True)
    pin = models.IntegerField()

    @property
    def get_phone_number(self):
        return "+234" + int(self.phone)

    @property
    def get_account_number(self):
        return "+234" + int(self.phone)

    def __str__(self):
        return self.user.username