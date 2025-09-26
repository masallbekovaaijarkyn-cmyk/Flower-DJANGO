from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Tag(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Which(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Flower(models.Model):
    name = models.CharField(max_length=200)  # аталышы
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # 1 гүл = 1 категория
    tags = models.ManyToManyField(Tag)  # көп тэг тандай алабыз
    which = models.ManyToManyField(Which)  # көп өлкө/кайдан тандай алабыз
    img_url = models.URLField()  # сүрөт шилтемеси
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Detail(models.Model):
    flower = models.OneToOneField(Flower, on_delete=models.CASCADE)  # 1 гүл = 1 деталь
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    product = models.CharField(max_length=100)

    def __str__(self):
        return f"Detail of {self.flower.name}"