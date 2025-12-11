from functools import wraps
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
# --------------------------------------------------------------------------------

# this  decorator  checks that user is owner or have access to this view or not


def owner_or_have_permission(model, perm=None):
    def decorator(view_fun):
        @wraps(view_fun)
        def wrapper(request, *arge, **kwargs):
            user = request.user
            obj = get_object_or_404(model, pk=kwargs.get('pk'))
            if getattr(obj, name="owner") == user:
                return view_fun(request, *arge, **kwargs)

            if user.has_perm(perm):
                return view_fun(request, *arge, **kwargs)

            raise PermissionDenied(
                "You do not have permission to access this.")
        return wrapper
    return decorator


class OwnerOrPermissionMixin(PermissionRequiredMixin):

    owner_field = "owner"

    def has_permission(self):
        user = self.request.user
        obj = self.get_object()

        try:
            if getattr(obj, self.owner_fielder) == user:
                print("owner is true")
                return True
        except:
            pass

        if self.permission_required and user.has_perm(self.permission_required):
            print("has permission")
            return True

        return False

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        raise PermissionDenied(self.permission_denied_message)


# ---------------------------------------------------------------------------------
