django-simple-currencies
===

django-simple-currencies allows you to define different currencies, and includes template tags / filters to allow easy conversion between them.

[![Latest Version](https://img.shields.io/pypi/v/django-simple-currencies.svg)](https://pypi.python.org/pypi/django-simple-currencies/)
[![Downloads](https://img.shields.io/pypi/dm/django-simple-currencies.svg)](https://pypi.python.org/pypi/django-simple-currencies/)
[![License](https://img.shields.io/github/license/bashu/django-simple-currencies.svg)](https://pypi.python.org/pypi/django-simple-currencies/)

## Setup

Either clone this repository into your project, or install with ```pip install django-simple-currencies```

You'll need to add ```currencies``` to ```INSTALLED_APPS``` in your project's ``settings.py`` file :

```python
INSTALLED_APPS = (
    ...
    'currencies',
)
```

Add ```currencies.middleware.CurrencyMiddleware``` to ```MIDDLEWARE_CLASSES```, must be after ```django.contrib.sessions.middleware.SessionMiddleware``` : 

```python
MIDDLEWARE_CLASSES = (
    ...    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'currencies.middleware.CurrencyMiddleware',  # must be after 'SessionMiddleware'
    ...
)
```

If you're going to use site-wide caching, add ```currencies.middleware.CacheCurrencyMiddleware```, but before ```django.middleware.cache.FetchFromCacheMiddleware``` : 

```python
MIDDLEWARE_CLASSES = (
    ...
    'currencies.middleware.CacheCurrencyMiddleware',  # must be before 'FetchFromCacheMiddleware'
    'django.middleware.cache.FetchFromCacheMiddleware',    
)
```

Be sure you have the `django.core.context_processors.request` context processor listed in ```TEMPLATE_CONTEXT_PROCESSORS``` : 

```python
TEMPLATE_CONTEXT_PROCESSORS = [
    ...
    "django.core.context_processors.request"
]
```

And don't forget to add this line to your site's root URLConf :

```python
url(r'^currencies/', include('currencies.urls')),
```

Then run ```./manage.py syncdb``` to create the required database tables


## Configuration

django-simple-currencies has built-in integration with [Open Exchange Rates](http://openexchangerates.org/)

You will need to specify your API key in your ```settings.py``` file :

```python
OPENEXCHANGERATES_APP_ID = "c2b2efcb306e075d9c2f2d0b614119ea"
```

You will then be able to use the management commands ``currencies`` and ``update_rates``. The former will import any currencies that are defined on [Open Exchange Rates](http://openexchangerates.org/). You can selectively import currencies, for example bellow command will import USD and EUR currencies only :

```shell
./manage.py currencies --import=USD --import=EUR
```

The ``update_rates`` management command will update all your currencies against the rates returned by [Open Exchange Rates](http://openexchangerates.org/). Any missing currency will be left untouched.

## Usage

First of all, load the ```currencies``` in every template where you want to use it :

    {% load currencies %}
    
to get a list of the active currencies :

    {% get_currencies as CURRENCIES %}
    
to get the currently set currency :

    {% get_current_currency as CURRENCY %}
    
and then to convert to a given currency :

    {% change_currency [amount] [currency_code] %}

or use the filter :

    {{ [amount]|currency:[currency_code] }}

Please see ```example``` application. This application is used to manually test the functionalities of this package. This also serves as a good example.

You need only Django 1.4 or above to run that. It might run on older versions but that is not tested.

