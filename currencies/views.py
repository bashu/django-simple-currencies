# -*- coding: utf-8 -*-

from django.utils.http import is_safe_url
from django.http import HttpResponseRedirect
from django.views.decorators.cache import never_cache

from .models import Currency
from .conf import SESSION_KEY


@never_cache
def set_currency(request):
    next, currency_code = (
        request.REQUEST.get('next'), request.REQUEST.get('currency_code', None))

    if not is_safe_url(url=next, host=request.get_host()):
        next = request.META.get('HTTP_REFERER')
        if not is_safe_url(url=next, host=request.get_host()):
            next = '/'

    response = HttpResponseRedirect(next)
    if code and Currency.active.filter(code=code).exists():
        if hasattr(request, 'session'):
            request.session[SESSION_KEY] = code
        else:
            response.set_cookie(SESSION_KEY, code)
    return response

