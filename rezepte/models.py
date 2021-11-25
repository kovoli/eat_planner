from django.db import models
from unidecode import unidecode
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        super(Category, self).save(*args, **kwargs)


class Recept(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = ProcessedImageField(upload_to='recept_images',
                                processors=[ResizeToFill(100,100)],
                                format='JPEG',
                                options={'quality': 100})
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    descripton = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        super(Recept, self).save(*args, **kwargs)




# class Week(models.Model):
#     week_number = models.SmallIntegerField()
#
#     def __str__(self):
#         return self.week_number
#
#
# class Day(models.Model):
#     day_name = models.CharField(max_length=255)
#     choise_week = models.ManyToManyField(Week, related_name='testing', blank=True)
#
#     def __str__(self):
#         return self.day_name
# Needed modules



