from rest_framework import permissions
from score.models import Profil


class CoachATeam(permissions.BasePermission):
    message = "Il faut diriger une équipe de la rencontre pour cette opération"

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        if request.method in permissions.SAFE_METHODS:
            return True

        print(request.user.is_authenticated)

        # Check if user is admin
        if request.user.is_superuser:
            return True

        # Check if user is anonymous
        if request.user.is_anonymous():
            return False

        # Check if user manage team
        try:
            if obj.equipeDom in request.user.profil.equipes.all():
                return True
            if obj.equipeExt in request.user.profil.equipes.all():
                return True
            return False
        except Profil.DoesNotExist:
            return False
