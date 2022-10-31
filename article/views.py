from django.shortcuts import render

import datetime
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse

from article.models import Article, Comment
from article.forms import CommentForm

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.

# Show Article Grid Page #
def article_page(request):
    data = Article.objects.all()
    context = {
        'article_posts': data,
        'username': request.user.username,
    }
    return render(request, 'article-blog.html', context)

# Show Write an Article Page #
@login_required(login_url='/login/')
def write_article_page(request):
    data = Article.objects.all()[:5]
    context = {
        'article_posts': data,
        'id': id,
        'username': request.user.username,
    }
    return render(request, 'write-article.html', context)

# Show Article Page by ID #
def article_page_by_id(request, id):
    data = Article.objects.get(id=id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            comment_form.save()

            comment = request.POST.get('comment_post')
            Comment.objects.create (
                art=data,
                user=request.user,
                comment_post=comment,
                artid=id
            )

            context = {
                'art_id': id,
                'comment_post': comment,
                'username': request.user.username
            }

            JsonResponse(context)
    
    rec = Article.objects.all()[:3]

    comments = None
    comment_form = CommentForm()

    if Comment.objects.filter(artid=id).exists():
        comments = Comment.objects.filter(artid=id)
    
    context = {
        'article_post': data,
        'recent_post': rec,
        'id': id,
        'username': request.user.username,
        'comment_form': comment_form,
        'comments': comments
    }

    return render(request, 'article-detail.html', context)

# Show JSON #
def show_json_article(request):
    data = Article.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_comment(request, artid):
    data = Comment.objects.get(id=artid)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Post a New Article #
@csrf_exempt
def post_article(request):
    if request.method == "POST":
        author = request.POST.get('author')
        title = request.POST.get('title')
        article_post = request.POST.get('article_post')
        date = datetime.datetime.now()
        like = 0
        data = Article.objects.create (
            user=request.user,
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

        response = JsonResponse(result)
        return response

def like(request, id):
    art = Article.objects.get(id=id)
    art.like += 1
    art.save()
    return HttpResponseRedirect(reverse('article:id', kwargs={'id':id}))

# def comment(request, id):
#     if request.method == 'POST':
#         comment_post = request.POST.get('comment_post')
#         art = Article.objects.get(id=id)
#         user = request.user
#         data = Comment.objects.create(
#             art=art,
#             user=user,
#             comment_post=comment_post
#         )

#         result = {
#             'pk': data.pk,
#             'fields': {
#                 'username': user.username,
#                 'comment_post': comment_post,
#                 'article': art
#             }
#         }

#         response = JsonResponse(result)

#     return