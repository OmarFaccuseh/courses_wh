from django.contrib import admin
from .models import Curso, Tema, Profile, Nota
from django.utils.html import format_html


class TemaAdmin(admin.StackedInline):
    model = Tema
    readonly_fields = ['TumbnailImage']
    extra = 0

    def TumbnailImage(self, obj):
        return format_html(obj.imagen.image(width=200))


class CourseAdmin(admin.ModelAdmin):
    inlines = [TemaAdmin]
    fields = ['name', 'descripcion', 'imagen', 'show_image', 'tags', 'cant_temas', 'categoria', 'tipo', 'calificacion',
              'stripe_product_id','stripe_price_id','stripe_price']
    readonly_fields = ['show_image', 'cant_temas',]
    
    def show_image(self, obj):
        return format_html(obj.imagen.image(width=500))


class NotaAdmin(admin.StackedInline):
    model = Nota
    extra = 1      


class ProfileAdmin(admin.ModelAdmin):
    inlines = [NotaAdmin]



# Register your models here.
admin.site.register(Curso, CourseAdmin)
admin.site.register(Profile, ProfileAdmin)

