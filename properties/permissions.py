from rest_framework import permissions

class IsAgentCanCreateProperty(permissions.BasePermission):
    message = "Only users who are agents can create properties."

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_agent:
            return True
        return False
