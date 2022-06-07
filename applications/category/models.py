from django.db import models

from applications.category.utils import slug_generator_title


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    slug = models.SlugField(max_length=255, primary_key=True, blank=True, unique=True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    def save(self, *agrs, **kwargs):
        self.slug = slug_generator_title(self.title)
        super(Category, self.save(args, kwargs))
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
