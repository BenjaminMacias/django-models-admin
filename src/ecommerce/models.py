from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from base.models import BasePublishModel
from .validators import validate_blocked_words

#TUPLA (VALOR_EN_DB, VALOR_PARA_USUARIO)
#PUBLISH_STATE_CHOICES = [
#    ("BR", "BORRADOR"),
#    ("PU", "PUBLICADO"),
#    ("PR", "PRIVADO"),
#]
# Create your models here.
##class ProductModel(models.Model):
class ProductModel(BasePublishModel):

##    class ProductStateOptions(models.TextChoices):
##        PUBLISHED = "PU", "PUBLICADO"
##        DRAFT = "BR", "BORRADOR"
##        PRIVATE = "PR", "PRIVADO"

##    state = models.CharField(max_length=2, choices=ProductStateOptions.choices, default=ProductStateOptions.DRAFT)
    title =models.TextField()
    price = models.FloatField()

    # Nuevos campos
    description = models.TextField(blank=True, null=True)
    seller = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    product_dimensions = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, db_index=True)

    def get_absolute_url(self):
        return f"/product/{self.slug}"
    



#class ProductModel(models.Model):
#    state = models.CharField(max_length=2, choices=PUBLISH_STATE_CHOICES, default="BR")
#    title =models.TextField()
#    price = models.FloatField()

    # Nuevos campos
#    description = models.TextField(blank=True, null=True)
#    seller = models.CharField(max_length=100, blank=True, null=True)
#    color = models.CharField(max_length=50, blank=True, null=True)
#    product_dimensions = models.CharField(max_length=100, blank=True, null=True)

##    def __str__(self):
##        return self.title
    
    def save(self, *args, **kwargs):
        validate_blocked_words(self.title)
        super().save(*args, **kwargs)

 #   def is_published(self):
 #       return self.state == "PU"
    
  ##  def is_published(self):
  ##      return self.state == self.ProductStateOptions.PUBLISHED

def slugify_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None or instance.slug == "":
        new_slug = slugify(instance.title)
        MyClass = instance.__class__
        qs = MyClass.objects.filter(slug__startswith=new_slug).exclude(id=instance.id)
        if qs.count() == 0:
            instance.slug = new_slug
        else:
            instance.slug = f"{new_slug}-{qs.count()+1}"

pre_save.connect(slugify_pre_save, sender=ProductModel)