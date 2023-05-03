import functools
from django.core.exceptions import PermissionDenied


def moderator_no_access(view_func):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.groups.filter(name="Moderator").exists():
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrapper


def moderator_only(view_func):
    @functools.wraps(view_func)
    def wrapper(request, *view_args, **view_kwargs):
        if request.user.groups.filter(name="Moderator").exists():
            return view_func(request, *view_args, **view_kwargs)
        else:
            raise PermissionDenied

    return wrapper
