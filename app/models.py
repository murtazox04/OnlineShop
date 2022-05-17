import sys

from django.contrib.auth import get_user_model
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.contenttypes.models import ContentType

# Create your models here.

User = get_user_model()

def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reversed(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})

class LatestProductManager:
    def get_pruducts_for_main_page(self, *args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        pruducts = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_pruducts = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            pruducts.extend(model_pruducts)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        pruducts, key=lambda x: x.__class__._meta.model_name.startwith(with_respect_to), reverse=True
                    )
        return pruducts

class LatestProduct:
    objects = LatestProductManager()

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    MIN_RESOLUTION = (400, 400)
    MAX_RESOLUTION = (400, 400)
    MAX_IMAGE_SIZE = 3145728

    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Product Title')
    slug = models.SlugField(unique=False)
    image = models.ImageField(verbose_name='Product Image')
    description = models.TextField(verbose_name='Product Description')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Product Price')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        image = self.image
        img = Image.open(image)
        new_img = img.convert('RGB')
        if new_img.height > self.MAX_RESOLUTION[0] or new_img.width > self.MAX_RESOLUTION[1]:
            resize_new_img = new_img.resize((400, 400), Image.ANTIALIAS)
            filestream = BytesIO()
            resize_new_img.save(filestream, format='JPEG', quality=90)
            filestream.seek(0)
            name = '{} . {}'.format(*self.image.name.split('.'))
            self.image = InMemoryUploadedFile(
                filestream,
                'ImageField',
                name,
                'image/jpeg',
                sys.getsizeof(filestream),
                None
            )

        super().save(*args, **kwargs)

class MenProduct(models.Model):
    size = models.CharField(max_length=255, verbose_name='Size')
    color = models.CharField(max_length=255, verbose_name='Color')
    quantity = models.IntegerField(verbose_name='Quantity')
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.size

class WomenProduct(models.Model):
    size = models.CharField(max_length=255, verbose_name='Size')
    color = models.CharField(max_length=255, verbose_name='Color')
    quantity = models.IntegerField(verbose_name='Quantity')
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.size

class User(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='First Name')
    last_name = models.CharField(max_length=255, verbose_name='Last Name')
    username = models.CharField(max_length=255, verbose_name='Username')
    email = models.EmailField(max_length=255, verbose_name='Email')
    password = models.CharField(max_length=255, verbose_name='Password')
    mobile = models.CharField(max_length=255, verbose_name='Mobile')

    def __str__(self):
        return self.username
