from django.urls import path
from article.views import article_page, write_article_page, show_json_article, post_article, article_page_by_id, like, delete_article, add_flutter, show_json_comment, add_comment_flutter

app_name = 'article'

urlpatterns = [
    path('', article_page, name='article'),
    path('write-article/', write_article_page, name='write'),
    path('json-article/', show_json_article, name='json'),
    path('show-article/<int:id>', article_page_by_id, name='id'),
    # path('post/', post_article, name='post'),
    path('like/<int:id>', like, name='like'),
    path('delete/<int:id>', delete_article, name='delete'),

    # recently added for flutter
    path('add-flutter/', add_flutter, name='addflutter'),
    path('json-comment/', show_json_comment, name='jsoncomment'),
    path('add-comment-flutter/', add_comment_flutter, name='addcomment')
]