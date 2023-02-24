import requests
from django.conf import settings
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FormModel


# Create your views here.

def validate_recaptcha(token):
    print(settings.RECAPTCHA_TOKEN)
    print({
        'secret': settings.RECAPTCHA_TOKEN,
        'response': token
    })
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
        'secret': settings.RECAPTCHA_TOKEN,
        'response': token
    })
    return r.json().get('success')


class FormView(APIView):
    class FormSerializer(serializers.ModelSerializer):
        class Meta:
            model = FormModel
            fields = '__all__'

    def post(self, request):
        data = request.data
        data['salary_range'] = ",".join(map(str, data.get('salary_range', '')))

        serializer = self.FormSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        is_valid = validate_recaptcha(serializer.validated_data['g_token'])

        serializer.save()
        return Response(is_valid)
