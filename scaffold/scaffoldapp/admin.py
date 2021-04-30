from django.contrib import admin
from . import models

# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display = ('titre', 'image', 'description')
    search_fields = ['titre']

class PrestationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'image')
    search_fields = ['titre']

class AboutAdmin(admin.ModelAdmin):
    list_display = ('image', 'titre', 'sous_titre')
    search_fields = ['titre']

class CardAdmin(admin.ModelAdmin):
    list_display = ('icone', 'titre', 'description', 'color')
    search_fields = ['titre']

class ImageAdmin(admin.ModelAdmin):
    list_display = ('categorie', 'image', 'titre', 'details', 'titre_details')
    search_fields = ['titre']

class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom']
    search_fields = ['nom']


admin.site.register(models.Banner,BannerAdmin)
admin.site.register(models.About, AboutAdmin)
admin.site.register(models.Prestation, PrestationAdmin)
admin.site.register(models.Card, CardAdmin)
admin.site.register(models.Image, ImageAdmin)
admin.site.register(models.Categorie, CategorieAdmin)
admin.site.register(models.Testimonial)
admin.site.register(models.Team)
admin.site.register(models.Partenaire)
admin.site.register(models.Pack)
admin.site.register(models.Avantage)
admin.site.register(models.Faq)
admin.site.register(models.Contact)
admin.site.register(models.Newsletter)
admin.site.register(models.Website)

