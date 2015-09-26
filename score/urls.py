from django.conf.urls import patterns, url, include
from score.views import DivisionViewSet, EquipeViewSet, RencontreViewSet, UserViewSet, ProfilViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'divisions', DivisionViewSet)
router.register(r'equipes', EquipeViewSet)
router.register(r'rencontres', RencontreViewSet)
router.register(r'users', UserViewSet)
router.register(r'profils', ProfilViewSet)

urlpatterns = patterns(
    'score.views',
    url(r'^api/', include(router.urls)),
    url(r'^$', 'home'),
    url(r'^upcoming', 'upcoming')
)
