from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
#request (всё, что мы получим от пользователя в качестве запроса через Интернет)
#{}, — это место, куда мы можем добавить что-нибудь для использования в шаблоне. Мы должны задавать имена передаваемым шаблону вещам

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
