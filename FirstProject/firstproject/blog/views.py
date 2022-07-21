from django.shortcuts import render
from django.utils import timezone
# 현재 directory에 있는 models.py 파일에 정의된 모델을 가져오기
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
    