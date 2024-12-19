from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog

# Create
def create_blog(request):
    data = {
        "title":"blog create",
        "name" : "Rokibul Hasan Rokib",
        "route" : "index.html"
    }
    return render(request, 'admin/modules/blog/index.html',data)

# Read (List)
def blog_list(request):
   
    return render(request, 'admin/modules/blog/index.html')

# Update
def update_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.save()
        return redirect('blog_list')
    return render(request, 'blog/update_blog.html', {'blog': blog})

# Delete
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('blog_list')
