import logging
logger = logging.getLogger(__name__)

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

__all__ = ['context_processor']

PROPERTY_ID_KEY = 'GOOGLE_ANALYTICS_PROPERTY_ID'
DISABLE = 'DISABLE_GOOGLE_ANALYTICS'

try:
    GA_PROPERTY_ID = getattr(settings, PROPERTY_ID_KEY)
except AttributeError:
    raise ImproperlyConfigured('Missing {}'.format(PROPERTY_ID_KEY))
else:
    logger.info('Google Analytics configured for ID {}'.format(GA_PROPERTY_ID))


def context_processor(request):
    """
    Use the variables returned in this function to render your Google Analytics
    tracking code template.
    """
    if getattr(settings, DISABLE, False) is True:
        logging.debug('Disabling Google Analytics due to {}'.format(DISABLE))
        return {}

    return {
        PROPERTY_ID_KEY: GA_PROPERTY_ID,
    }
