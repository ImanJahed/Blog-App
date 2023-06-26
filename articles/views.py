from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.urls import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied

from .models import Article
from .forms import CommentForm

# Create your views here.
class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "article/article_list.html"


class CommentGet(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article/article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm 
        return context
    

class CommentPost(SingleObjectMixin, FormView):
    model = Article
    form_class = CommentForm
    template_name = 'articles/article_detail.html'
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.get_object()
        return reverse('article-detail', kwargs={'pk': article.pk})


class ArticleDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request,*args, **kwargs)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ("title", "body")
    template_name = "article/article_new.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ["title", "body"]
    template_name = "article/article_edit.html"

    permission_denied_message = "Hooo!"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return HttpResponse("<h1> You can not edit this article</h1>")


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article/article_delete.html"
    success_url = reverse_lazy("article-list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
