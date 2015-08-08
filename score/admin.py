from django.contrib import admin
from score.models import Division, Equipe, Rencontre

admin.site.register(Equipe)
admin.site.register(Division)
admin.site.register(Rencontre)