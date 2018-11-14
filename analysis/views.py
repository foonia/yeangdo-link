from django.shortcuts import render


def index(request):
    return render(request, 'analysis/index.html')


def show_plot(request):
    return render(request, 'analysis/show_plot.html')


def submit_data(request):
    return render(request, 'analysis/submit_data.html')

 
def more_info(request):
    return render(request, 'analysis/more_info.html')