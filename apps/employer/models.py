from django.db.models import *
from image_optimizer.fields import OptimizedImageField

class Employer(Model):
    name=CharField(
        'Employer name',
        max_length=256
    )

    about=TextField(
        'About employer',
        blank=True,
        null=True
    )

    foundation_date=PositiveSmallIntegerField(
        'Date of foundation of the company',
    )

    email=EmailField(
        'Email'
    )

    number=CharField(
        'Number',
        max_length=13
    )

    company_photo=OptimizedImageField(
        verbose_name='Company logo',
        upload_to='employer-photos/%Y/%m/%d',
        optimized_image_output_size=(500,500),
        optimized_image_resize_method='cover'
    )

    city=CharField(
        'Location of the company',
        max_length=128
    )

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name='Employer'
        verbose_name_plural='Employers'
