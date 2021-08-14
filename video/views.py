from django.shortcuts import get_object_or_404, redirect, render
from .models import CategoryList,Item, VideoComment
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from video.templatetags import extras



# Create your views here.
# def index(request):
#     # productarr=Products.objects.all()
#     return render(request,'blog/index.html')






def newcategory_list(request):
    # category=None
    categories=CategoryList.objects.all()
    # article=Item.objects.all()
    return render(request,'video/categorylist.html',{'categories':categories})





# def category_view(request,category_slug):
#     category=get_object_or_404(CategoryList,slug=category_slug)
#     article=Item.objects.filter(category=category)
#     context={'category':category,'article':article}
#     return render(request,'video/category_view.html',context)

def category_view(request,category_slug):
    category=CategoryList.objects.filter(slug=category_slug).first()
    article=Item.objects.filter(category=category)
    print("I am called")
    return render(request,'video/category_view.html',{'article':article,'category':category})

# def article_detail(request,article_slug):
#     article=get_object_or_404(Item,slug=article_slug)

#     context={
#         'article':article
#         }    
#     return render(request,'video/article_detail.html',context)
def article_detail(request,article_slug):
    article=Item.objects.filter(slug=article_slug).first()
    comments=VideoComment.objects.filter(article=article,parent=None)
    replies=VideoComment.objects.filter(article=article).exclude(parent=None)
    repDict={}
    for reply in replies:
        if reply.parent.srno not in repDict.keys():
            repDict[reply.parent.srno]=[reply]
        else:
            repDict[reply.parent.srno].append(reply)

    
    context={'article':article,'comments':comments,'user':request.user,'repDict':repDict}
    print("Now I am called")
    return render(request,'video/article_detail.html',context)


def postComment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user = request.user
        articleSno = request.POST.get("articleSno")
        article=Item.objects.get(sno=articleSno)
        parentSno=request.POST.get("parentSno")
        if parentSno=="":
            comment=VideoComment(comment=comment,user=user,article=article)
            comment.save()
            messages.success(request,"Your comment has been posted successfully")
        else:
            parent=VideoComment.objects.get(srno=parentSno)
            comment=VideoComment(comment=comment,user=user,article=article,parent=parent)

        
            comment.save()
            messages.success(request,"Your reply has been posted successfully")

    
    return HttpResponseRedirect(reverse('video:article_detail', args=(article.slug,)))

# Create your views here.


