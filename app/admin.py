from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.utils.safestring import mark_safe

# Register your models here.
from app.models import *

class MenAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe("<span style='color:red; font-size:17px;'>Minimum resolution: {}x{"
                                                   "}").format(*Product.MIN_RESOLUTION)

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Image size must be less than 3mb')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Image resolution is too low')
        if img.height > max_height or img.width > max_width:
            raise ValidationError('Image resolution is too high')
        return image

class MenAdmin(admin.ModelAdmin):
    form = MenAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='mens'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class WoMenAdminForm(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='womens'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Product)
# admin.site.register(MenProduct)
# admin.site.register(WomenProduct)
admin.site.register(Category)
admin.site.register(User)
