from django.urls import path
from mysite import views
from mysite.views import PostListView, PostDetailView,PostCreateView,PostUpdateView, PostDeleteView

urlpatterns = [
    #path('',views.home,name='blog-home'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/new',PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('',PostListView.as_view(),name='post_list'),
    path('about/',views.about,name='about_page'),
]
