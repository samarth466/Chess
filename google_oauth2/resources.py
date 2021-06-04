from tastypie.resources import ModelResource
from .models import GoogleTokens


class GoogleTokensResource(ModelResource):
    class Meta:
        queryset = GoogleTokens.objects.all()
        resource_name = 'googletokens'