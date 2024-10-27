from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
      STATUS = (
          ('True', 'Evet'),
          ('False', 'Hayir')


      )
      title = models.CharField(max_length=100) # blank=True alanın  boş bırakılabildigini , blank=False olduğunda ise bu alanın formda doldurulması zorunludur.
      keyword =models.CharField(blank=True,max_length=250)
      description = models.CharField(blank=True,max_length=250)
      image = models.ImageField( blank=True,upload_to='images/')
      status = models.CharField(blank=True,max_length=250,choices=STATUS)
      slug = models.SlugField(blank=True,unique=True)
      parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)



class Product(models.Model):
    STATUS=(('True', 'Evet'),('False', 'Hayir'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #bagli olan satırı sil
    title = models.CharField(max_length=100)
    keyword = models.CharField(blank=True,max_length=250)
    description = models.CharField(blank=True,max_length=250)
    image = models.ImageField(upload_to='images/')

    #price = models.DecimalField(max_digits=10, decimal_places=2)
    price= models.FloatField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    details = models.TextField()
    status = models.CharField(blank=True,max_length=250,choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True,unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

      def __str__(self):
          return self.title
      def __str__(self):
          return self.title