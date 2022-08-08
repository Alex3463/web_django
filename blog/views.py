from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    # 가장최근 포스팅 부터 리스트
    ordering = '-pk' 
    
class PostDetail(DetailView):
    model = Post

# Create your views here.
