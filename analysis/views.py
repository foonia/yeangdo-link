from django.shortcuts import render


def data_analysis(request):
    return render(request, 'analysis/data_analysis.html')


def more_info(request):
    return render(request, 'analysis/more_info.html')