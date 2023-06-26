from django.urls import path

from . import views


urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-list'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('new', views.ArticleCreateView.as_view(), name='article-new'),
    path('<int:pk>/edit', views.ArticleUpdateView.as_view(), name='article-edit'),
    path('<int:pk>/delete', views.ArticleDeleteView.as_view(), name='article-delete'),
]

