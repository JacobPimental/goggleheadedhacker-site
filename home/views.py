from django.shortcuts import render
from blog.models import Post, Category
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
import math

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# Create your views here.
@cache_page(CACHE_TTL)
@csrf_protect
def index(request, page_num):
    num_posts = Post.objects.all().count()
    max_pages = math.ceil(num_posts/5)
    print(page_num)
    if page_num == '':
        return HttpResponseRedirect('/1')
    if max_pages == 0:
        return HttpResponseRedirect('/blog/no_results')
    if int(page_num) > max_pages:
        return HttpResponseRedirect('/blog/no_results')
    start = (int(page_num)-1)*5
    end = (int(page_num))*5
    posts = Post.objects.filter(is_draft=False).order_by('-pub_date')[start:end]
    return render(request, 'home/index.html', {'posts':posts,
                                               'cur_page':int(page_num),
                                               'max_pages':max_pages,
                                               'prev_page':int(page_num)-1,
                                               'next_page':int(page_num)+1,
                                               'title':'Goggle Headed Hacker'})
