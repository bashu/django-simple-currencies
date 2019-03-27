# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.cache import patch_vary_headers
from django.utils.deprecation import MiddlewareMixin

from .utils import get_currency_code
from .conf import SESSION_KEY


class CurrencyMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if not hasattr(request, 'session'):
            return

        # make sure that currency was initialized
        if not SESSION_KEY in request.session or request.session[SESSION_KEY] is None:
            request.session[SESSION_KEY] = get_currency_code(False)


class CacheCurrencyMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.META['HTTP_X_CURRENCY'] = get_currency_code(
            request) or 'UNKNOWN'

    def process_response(self, request, response):
        if 'X-Currency' not in response:
            response['X-Currency'] = get_currency_code(
                request) or 'UNKNOWN'

        patch_vary_headers(response, ['X-Currency'])
        return response
