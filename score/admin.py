from django.contrib import admin
from solo.admin import SingletonModelAdmin
from score.models import Division, Equipe, Rencontre, Profil, SiteConfiguration
from score.forms import SiteConfigurationForm


class RencontreAdmin(admin.ModelAdmin):
    # Edition de la grille
    list_display = (
        'numero',
        'date',
        'heure',
        'equipeDom',
        'equipeExt',
        'scoreDom',
        'forfaitDom',
        'scoreExt',
        'forfaitExt'
    )
    list_filter = ('date', 'heure', 'equipeDom', 'equipeExt')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('equipeDom__nom', 'equipeExt__nom')

    # Edition du formulaire
    fieldsets = (
        ('General', {
            'description': 'Informations sur la rencontre',
            'fields': ('numero', 'date', 'heure')
        }),
        ('Equipes', {
            'description': 'Les opposants',
            'fields': ('equipeDom', 'equipeExt')
        }),
        ('Score', {
            'description': 'Résultats de la rencontre',
            'fields': ('scoreDom', 'forfaitDom', 'scoreExt', 'forfaitExt')
        })
    )


class EquipeAdmin(admin.ModelAdmin):
    # Edition de la grille
    list_display = (
        'nom',
        'division'
    )
    list_filter = ('nom', 'division')
    ordering = ('nom',)
    search_fields = ('nom', 'division__nom')


class ProfilAdmin(admin.ModelAdmin):
    # Edition de la grille
    list_display = (
        'user',
        'apercu_equipes'
    )
    list_filter = ('user', 'equipes')
    ordering = ('user',)
    search_fields = ('user',)

    def apercu_equipes(self, profil):
        return ', '.join(e.nom for e in profil.equipes.all())

    # En-tête de notre colonne
    apercu_equipes.short_description = 'Equipes'


class EquipeInline(admin.TabularInline):
    model = Equipe
    extra = 3


class DivisionAdmin(admin.ModelAdmin):
    inlines = [EquipeInline]


# SingletonModelAdmin already extends admin.ModelAdmin
class SiteConfigurationAdmin(SingletonModelAdmin):
    form = SiteConfigurationForm

    # Edition du formulaire
    fieldsets = (
        ('FFBB', {
            'description': 'Paramètres pour l\'import sur FFBB',
            'fields': ('login', 'password', 'url_ffbb')
        }),
    )


admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Rencontre, RencontreAdmin)
admin.site.register(Profil, ProfilAdmin)
admin.site.register(SiteConfiguration, SiteConfigurationAdmin)
