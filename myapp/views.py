import pygal as pygal
from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Portfolio,Category


# Create your views here.

def index(request):
    all_projects = Portfolio.objects.all()
    categories = Category.objects.all()
    data = {}
    for category in categories:
        project_list = Portfolio.objects.filter(category_id=category.id).all()
        data[category.name]=len(project_list)

    pie_chart = pygal.Pie()
    pie_chart.title = 'Total projects in 2024 (in %)'
    for i in data:
        pie_chart.add(i,data[i])
    context = {"projects": all_projects,
               "pie_chart": pie_chart.render_data_uri()}
    # return HttpResponse(pie_chart.render())
    return render(request, 'index.html', context)


def inner(request):
    return render(request, 'inner-page.html')


def portfolio(request, id):
    project = Portfolio.objects.get(id=id)
    context = {"project": project}
    return render(request, 'portfolio-details.html', context)
