from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# ShortCuts
class Shortcuts(models.Model):
    Shortcut_id = models.BigAutoField(primary_key=True)
    Name = models.CharField(null=True, max_length=30)
    Description = models.TextField(null=True, max_length=255)
    Is_Enable =  models.IntegerField(null=True)
    Shortcut_type = models.IntegerField(null=True)
    Company_id = models.ForeignKey(
        'Company', related_name='Company_ref' ,null=True,
        on_delete=models.CASCADE,
    )
    Created_on = models.DateTimeField(null=True)
    Created_by = models.IntegerField(null=True)
    Updated_on = models.DateTimeField( null=True)
    Updated_by = models.IntegerField(null=True)


# Enterprise , Company
class Company(models.Model):
    Company_id = models.BigAutoField(primary_key=True)
    Name = models.TextField(max_length=30, null=True, blank=True)
    Description = models.TextField(max_length=250, blank=True)
    Company_type = models.IntegerField(null=True, blank=True)
    created_on  = models.DateField(null=True, blank=True)
    created_by = models.IntegerField(null=True,blank=True)
    Updated_on = models.DateField(null=True, blank=True)
    Updated_by = models.IntegerField(null=True,blank=True)

class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.TextField(max_length=20, blank=True)
    created_on  = models.DateField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    Updated_on = models.DateField(null=True, blank=True)
    Updated_by = models.IntegerField(null=True, blank=True)
    Company_id = models.ForeignKey(
        'Company', related_name='Company_no' ,null=True,
        on_delete=models.CASCADE,
    )
    


#this method to generate profile when user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Userprofile.objects.create(user=instance)

#this method to update profile when user is updated
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()