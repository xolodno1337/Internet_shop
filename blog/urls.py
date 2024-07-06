from django.conf.urls.static import static
from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, toggle_active
from django.conf import settings

app_name = BlogConfig.name

urlpatterns = [
    path("create/", BlogCreateView.as_view(), name="create"),
    path("list/", BlogListView.as_view(), name="blog_list"),
    path("view/<int:pk>/", BlogDetailView.as_view(), name="view"),
    path("edit/<int:pk>/", BlogUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>/", BlogDeleteView.as_view(), name="delete"),
    path('toggle/<int:pk>/', toggle_active, name='toggle_active'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
