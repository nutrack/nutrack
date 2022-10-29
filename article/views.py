from django.shortcuts import render

import datetime
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.urls import reverse

from article.models import Article

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Show Article Page #
def article_page(request):
    data = Article.objects.all()
    context = {
        'article_posts': data,
        'username': request.user.username,
    }
    return render(request, 'article-blog.html', context)

# Show Article Page #
def write_article_page(request):
    data = Article.objects.all()[:5]
    context = {
        'article_posts': data,
        'username': request.user.username,
    }
    return render(request, 'write-article.html', context)

# Show Article Page #
def article_page_by_id(request, id):
    data = Article.objects.get(id=id)
    context = {
        'article_post': data,
        'username': request.user.username,
    }
    return render(request, 'article-detail.html', context)

# Show JSON #
def show_json_article(request):
    data = Article.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Post a New Article (Add an Article) #
@csrf_exempt
def post_article(request):
    print("nyampe sini gasi")
    if request.method == "POST":
        author = request.POST.get('author')
        title = request.POST.get('title')
        print(title)
        article_post = request.POST.get('article_post')
        print(article_post)
        date = datetime.datetime.now()
        like = 0
        # share = 0
        data = Article.objects.create (
            author=author,
            date=date, 
            like=like,
            title=title, 
            article_post=article_post
        )
        result = {
            'pk': data.pk,
            'fields':{
                'author': author,
                'date': date,
                'like': like,
                'title': title,
                'article_post': article_post
            }
        }
        return JsonResponse(result)