from django.db import models

class shop(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.title

class category(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    shop = models.ForeignKey(shop,on_delete=models.CASCADE)
    desc = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
class product(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    description = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    amount = models.IntegerField(default=0)
    price = models.FloatField()
    image = models.ImageField(upload_to=None,null=False,blank=False)
    active = models.BooleanField(default=False)
    category = models.ManyToManyField(category,null=True)
    shop = models.ForeignKey(shop,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.title
    
