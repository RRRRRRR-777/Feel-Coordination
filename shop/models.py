from django.db import models
from django.urls import reverse
from django.shortcuts import render


class PostTag(models.Model):
    name = models.CharField(max_length=200, unique=False)
    
    def __str__(self):
        return self.name


# 個別商品
class Detail_tag(models.Model):
    name = models.CharField(max_length=250, unique=False)

    def __str__(self):
        return self.name

class Detail(models.Model):
    class Meta:
        db_table = "detail"
    
    name = models.CharField(verbose_name='商品', max_length=255)
    slug = models.SlugField(verbose_name='URLに表示される名前', max_length=250, unique=False)
    description = models.TextField(verbose_name='商品説明')
    price = models.IntegerField(verbose_name='価格')
    image = models.ImageField(upload_to='detail/image')
    file = models.FileField(upload_to='detail/file', blank=True)
    stock = models.IntegerField(verbose_name='在庫')
    created = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(PostTag, blank=True)
    subtag = models.ManyToManyField(Detail_tag, blank=True)
    baroname1 = models.CharField(max_length=150, blank=True, null=True, default='光沢感')
    baroint1 = models.IntegerField(blank=True, default=True,null=True)
    baroname2 = models.CharField(max_length=150, blank=True, null=True, default='伸縮性')
    baroint2 = models.IntegerField(blank=True, default=True,null=True)
    baroname3 = models.CharField(max_length=150, blank=True, null=True, default='透け感')
    baroint3 = models.IntegerField(blank=True, default=True,null=True)
    
    def get_url(self):
        return reverse('shop:product_detail', args=[self.slug])

    def __str__(self):
        return self.name




# コーディネート



def image_path(instance, filename):
    ext = filename.split('.')[-1]
    new_name = instance.name
    return f'producthover/{new_name}.{ext}'

class ValidManager(models.Manager):
    def get_query(self):
        return super(ValidManager, self).get_queryset().filter(available=True)

class Product(models.Model):
    name = models.CharField(verbose_name='コーディネート名', max_length=250, unique=True)
    slug = models.SlugField(verbose_name='URLに表示される名前', max_length=250, unique=False)
    description = models.TextField(verbose_name='説明', blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='prodcut/image', blank=True)
    file = models.FileField(upload_to='product/file', blank=True)
    detail = models.ManyToManyField(Detail)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField(PostTag, blank=True)

    objects = models.Manager()

    valid_objects = ValidManager()

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('shop:product_detail', args=[self.slug])

    def index(request):
        image_request = request.user.set_image_path
        return render(request, 'shop/base.html', {'image_request': image_request}) 

