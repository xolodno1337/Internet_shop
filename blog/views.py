from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


def toggle_active(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.is_active = not blog.is_active
    blog.save()
    return redirect('blog:blog_list')


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "body", "image", "is_active")
    success_url = reverse_lazy("blog:blog_list")

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset.filter(is_active=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "body", "image", "is_active")

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:view", args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")
