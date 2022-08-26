from django.shortcuts import render
from mysite.models import Post
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

#def home(request):
#    context = {
#        'posts': Post.object.all()
#    }
#    return render(request, 'mysite/home.html', context)
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        if self.request.user == post.author:
            return True
        return False
    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




class PostListView(ListView):
    model = Post
    # context_object_name = 'object_list'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

def about(request):
    return render(request, 'mysite/about.html', {'title':'About'})
