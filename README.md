# Django Google Analytics

Thanks to [http://www.nomadblue.com/blog/django/google-analytics-tracking-code-into-django-project/](http://www.nomadblue.com/blog/django/google-analytics-tracking-code-into-django-project/) for inspiration.

## Install

Add these settings to your settings file:

```
GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-12345678-1'
```

Add the template context processor to Django's default ones

```
from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    ('yourproject.libs.google_analytics.context_processor',)
)
```

For any pages you want to track, insert this template code just before the
closing `</body>` tag:

```
{% include "google_analytics.html" %}
```

**NOTE** By default Google Analytics is always on: you might want to turn it
off in development and/or staging.

## Disabling Google Analytics

You can disable Google Analytics by setting `DISABLE_GOOGLE_ANALYTICS = True`

If you want to disable based on an environment variable, you could do something
like the following in your settings file:

```
DISABLE_GOOGLE_ANALYTICS = os.environ.get('DISABLE_GOOGLE_ANALYTICS', 'false') == 'true'
```

Or you might want to disable when in `DEBUG` mode:

```
DISABLE_GOOGLE_ANALYTICS = DEBUG
```
