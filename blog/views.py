from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from .models import Post, Category
import re, math
# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def blog_category(request, cat_id, page_num):
    category = get_object_or_404(Category, pk=cat_id)
    num_posts = Post.objects.filter(my_category=category).distinct().count()
    max_pages = math.ceil(num_posts/5)
    if max_pages == 0:
        return HttpResponseRedirect('/blog/no_results')
    if int(page_num) > max_pages:
        return HttpResponseRedirect('blog/category/'+cat_id+'/'+str(max_pages))
    start = (int(page_num)-1)*5
    end = (int(page_num))*5
    posts = Post.objects.filter(my_category=category).order_by('-pub_date').distinct()
    return render(request, 'blog/listing.html', {'posts':posts,
                                                 'cur_page':int(page_num),
                                                 'max_pages':max_pages,
                                                 'prev_page':int(page_num)-1,
                                                 'next_page':int(page_num)+1,
                                                 'title':category.cat_name})


@cache_page(CACHE_TTL)
@vary_on_cookie
@csrf_protect
def blog_detail(request, post_id):
    print('blog_detail')
    post = get_object_or_404(Post, pk=post_id, is_draft=False)
    post.views += 1
    post.save()
    return render(request, 'blog/detail_view.html', {'post':post,
                                                     'title':post.title,
                                                     'description':post.description})

def searching(request):
    if request.method == "POST":
        print('received post')
        print(request.POST.dict())
        search = request.POST.dict()['search']
        search = re.sub('[^A-Za-z0-9 ]+', '', search)
        return_url = ('/blog/search/'+
                      search+
                      '/1/')
        return HttpResponseRedirect(return_url)
    else:
        return HttpResponseRedirect('/')

def blog_search(request, search_str, page_num):
    print('blog_search')
    num_posts = Post.objects.filter((
                                Q(title__contains=search_str) |
                                Q(tags__tag_name__contains=search_str) |
                                Q(content__contains=search_str)),
				is_draft=False
                               ).distinct().count()
    max_pages = math.ceil(num_posts/5)
    if max_pages == 0:
        return HttpResponseRedirect('/blog/no_results')
    if int(page_num) > max_pages:
        return HttpResponseRedirect('/blog/search/'+search_str+'/'+str(max_pages))
    start = (int(page_num)-1)*5
    end = (int(page_num))*5
    posts = Post.objects.filter((
                                Q(title__contains=search_str) |
                                Q(tags__tag_name__contains=search_str) |
                                Q(content__contains=search_str)),
				is_draft=False
                               ).distinct()[start:end]
    return render(request, 'blog/listing.html', {'posts':posts,
                                                 'cur_page':int(page_num),
                                                 'max_pages':max_pages,
                                                 'prev_page':int(page_num)-1,
                                                 'next_page':int(page_num)+1,
                                                 'title':search_str})

def blog_tag_search(request, tag_str, page_num):
    print('length is: ' + str(len(tag_str)))
    if len(tag_str)>50:
        return HttpResponseRedirect('/blog/no_results')
    print('tag_search')
    num_posts = Post.objects.filter(
        tags__tag_name__contains=tag_str, is_draft=False).distinct().count()
    max_pages = math.ceil(num_posts/5)
    if max_pages == 0:
        return HttpResponseRedirect('/blog/no_results')
    if int(page_num) > max_pages:
        return HttpResponseRedirect('/blog/search/tag/'+tag_str+'/'+str(max_pages))
    start = (int(page_num)-1)*5
    end = (int(page_num))*5
    posts = Post.objects.filter(
        tags__tag_name__contains=tag_str, is_draft=False).distinct()[start:end]
    return render(request, 'blog/listing.html', {'posts':posts,
                                                 'cur_page':int(page_num),
                                                 'max_pages':max_pages,
                                                 'prev_page':int(page_num)-1,
                                                 'next_page':int(page_num)+1,
                                                 'title':tag_str})

def no_results(request):
    print('no results')
    return render(request, 'blog/no_results.html', {'title':'No Results'})
