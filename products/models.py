from django.db import models

# Create your models here.
class Category(models.Model):
     name=models.CharField(max_length=150,db_index=True)
     img=models.ImageField(upload_to='pics',blank=True)
     slug=models.SlugField(unique=True)
     class Meta:
        ordering=('-name',)
     def __str__(self):
        return self.name

class Products(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name= models.CharField(max_length=150)
    desc= models.TextField()
    price=models.IntegerField()
    img=models.ImageField(upload_to='pics')
    desc1=models.TextField()
    desc2=models.TextField()
    specialOffer=models.BooleanField(default=False)
    producturl=models.URLField(max_length=40)

    class Meta:
        ordering=('-name',)
    def __str__(self):
        return self.name