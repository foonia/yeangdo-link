import json
import urllib.parse

from django.http.response import JsonResponse
from rest_framework import generics
from rest_framework import filters

from analysis.models import Survey
from .serializers import SurveySerializer

from analysis import datas


# class SurveyViewSet(viewsets.ModelViewSet):
#     queryset = Survey.objects.all()
#     serializer_class = SurveySerializer


class SurveyListApiView(generics.ListAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = ('id',)

    def get_queryset(self):
        queryset = Survey.objects.all()
        address = self.request.query_params.get('address', None)
        occupation = self.request.query_params.get('occupation', None)

        if address is not None:
            queryset.filter(address=address)
        elif occupation is not None:
            queryset = queryset.filter(desired_occupation1=occupation)

        return queryset


def bar_api_view(request):
    return JsonResponse(datas.bar_data, safe=False)


def chart_api_view(request):
    return JsonResponse(datas.chart_data, safe=False)


def curve_api_view(request):
    return JsonResponse(datas.curve_data, safe=False)


def candle_api_view(request):
    return JsonResponse(datas.candle_data, safe=False)
