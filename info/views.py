from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from info.forms import NewsForm
from info.models import News


def news_list(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'news_list.html', context)


def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Новость успешно добавлена</h2>"
                                "<a href='../news'>вернуться к списку новостей</a>")
    else:
        form = NewsForm()
        return render(request, 'add_news.html', {'form': form})


def delete_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    news.delete()
    return HttpResponse("<h2>Новость успешно удалена</h2>"
                        "<a href='../../'>вернуться к списку новостей</a>")


def edit_news(request, news_id):
    news = get_object_or_404(News, id=news_id)

    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Новость успешно изменена</h2>"
                                "<a href='../../'>вернуться к списку новостей</a>")
    else:
        form = NewsForm(instance=news)

    return render(request, 'edit_news.html', {'form': form, 'news': news})
