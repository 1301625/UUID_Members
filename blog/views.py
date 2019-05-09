from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect ,get_object_or_404
# Create your views here.

def post_list(request):
    qs = Post.objects.all()
    return render(request , 'blog/post_list.html',{
        'post_list':qs
    })
def post_detail(request, pk):
    post =get_object_or_404(Post,pk=pk)
    return render(request, 'blog/post_detail.html',
                  {'post':post,})


def post_new(request ,post=None):
    if request.method =='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()
        return render(request, 'blog/post_new.html' ,{
            'form':form,
        })


