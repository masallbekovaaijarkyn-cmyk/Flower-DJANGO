from django.db import models

# Create your models here.
class About_us(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField()
    adres = models.CharField(max_length=100,blank=True,null=True)
    adres_url = models.URLField(blank=True,null=True)
    phone = models.CharField(max_length=100,blank=True,null=True)
    ins_url = models.URLField(blank=True,null=True)
    whats_url = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.email