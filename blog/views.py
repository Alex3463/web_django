from django.shortcuts import render
from unicodedata import category
from django.views.generic import ListView, DetailView
from .models import Post, Category

class PostList(ListView):
    model = Post
    # 가장최근 포스팅 부터 리스트
    ordering = '-pk' 

    def get_context_data(self, **kwargs):
        context = super(PostList,self).get_context_data()
        context['categories'] = Category.objects.all()
        context["no_category_post_count"] = Post.objects.filter(category=None).count() 
        return context
    
    
class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail,self).get_context_data()
        context['categories'] = Category.objects.all()
        context["no_category_post_count"] = Post.objects.filter(category=None).count() 
        return context

   
def category_page(request,slug):
        if slug == 'no_category':
            category = '미분류'
            post_list = Post.objects.filter(category=None)
        else:
            category = Category.objects.get(slug=slug)
            post_list = Post.objects.filter(category=category)
    
        return render(
            request,
            'blog/post_list.html',
            {
                'post_list' : post_list,
                'categories' : Category.objects.all(),
                'no_category_post_count' : Post.objects.filter(category=None).count(),
                'category' : category

            }
        )
# Create your views here.
