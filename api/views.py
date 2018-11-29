import json
from django.http.response import JsonResponse
from rest_framework import viewsets
from rest_framework import generics

from analysis.models import Survey
from .serializers import SurveySerializer

from analysis import datas


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class SurveyListApiView(generics.ListAPIView):
    queryset = Survey.objects.all()
    default_list = [0, 0, 0, 0]

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        years = {'1950': SurveyListApiView.default_list[:], '1960': SurveyListApiView.default_list[:],
                 '1970': SurveyListApiView.default_list[:], '1980': SurveyListApiView.default_list[:],
                 '1990': SurveyListApiView.default_list[:], '2000': SurveyListApiView.default_list[:],
                 '2010': SurveyListApiView.default_list[:]}

        for query in queryset.values():
            birth = query.get('birth_date')
            final_edu = query.get('final_education')

            print(years)

            years[str(birth.year)[:3]+'0'][SurveyListApiView.check_education(final_edu)] += 1

        return JsonResponse({'result': [{'year': year[0], 'data': year[1]} for year in years.items()]})

    @classmethod
    def check_education(cls, edu):
        if edu == 'e':
            return 0
        elif edu == 'm':
            return 1
        elif edu == 'h':
            return 2
        else:
            return 3


def bar_api_view(request):
    return JsonResponse(datas.bar_data, safe=False)


def chart_api_view(request):
    return JsonResponse(datas.chart_data, safe=False)


def curve_api_view(request):
    return JsonResponse(datas.curve_data, safe=False)


def candle_api_view(request):
    return JsonResponse(datas.candle_data, safe=False)
