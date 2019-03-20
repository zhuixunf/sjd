from django.shortcuts import render
from .models import Post
from .forms import PostForm
# Create your views here.
def post_update(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post_form = PostForm(data=request.POST, instance=post)
        post_form.save()
        return redirect('/')
    else:
        post_form = PostForm(instance=post)
    return render(request, 'post_update.html', {'post_form': post_form})
