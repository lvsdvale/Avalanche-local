from .mdetect import UAgentInfo
from django.utils.deprecation import MiddlewareMixin
from Avalanche import settings

class MobileDetectionMiddleware(MiddlewareMixin):
    """
    Useful middleware to detect if the user is
    on a mobile device.
    """
    def process_request(self, request):
        is_mobile = False
        is_tablet = False
        is_phone = False

        user_agent = request.META.get("HTTP_USER_AGENT")
        http_accept = request.META.get("HTTP_ACCEPT")
        if user_agent and http_accept:
            agent = UAgentInfo(userAgent=user_agent, httpAccept=http_accept)
            is_tablet = agent.detectTierTablet()
            is_phone = agent.detectTierIphone()
            is_mobile = is_tablet or is_phone or agent.detectMobileQuick()

        request.is_mobile = is_mobile
        request.is_tablet = is_tablet
        request.is_phone = is_phone
        request.is_production = not settings.DEBUG