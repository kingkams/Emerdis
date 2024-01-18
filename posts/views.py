from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView  ,View
from .models import AssemblyPost, PeoplePosts
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PeoplePosts, AssemblyPost
from django.template.defaultfilters import truncatewords
from .forms import CreatePostForm, CreateAnnouncementForm


class AnnoucementView(LoginRequiredMixin, ListView):
    model = AssemblyPost
    template_name = "PeoplePage/Annoucements.html"
    context_object_name = "assembly"


class PeoplelistView(LoginRequiredMixin, ListView):
    model = PeoplePosts
    template_name = "PeoplePage/list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return PeoplePosts.objects.filter(author=self.request.user)


class CreatePost(LoginRequiredMixin, CreateView):
    form_class = CreatePostForm
    template_name = "PeoplePage/create.html"
    success_url = reverse_lazy('post:Posts')



    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)

class PostDetail(LoginRequiredMixin,DetailView):
    model = PeoplePosts
    context_object_name ='post'
    template_name = "PeoplePage/detail.html"

class DeletePost(LoginRequiredMixin, DeleteView):
    model = PeoplePosts
    context_object_name = 'post'
    template_name = "PeoplePage/dlete.html"
    success_url = reverse_lazy('post:Posts')

class DeleteAnnouncement(LoginRequiredMixin,DeleteView):
    model = AssemblyPost
    template_name = "AssemblyPage/delete.html"
    success_url = reverse_lazy('post:announcements')
class AssemblyList(LoginRequiredMixin, ListView):
    model = PeoplePosts
    template_name = "AssemblyPage/List.html"
    context_object_name = "posts"


class AnnouncementDetails(LoginRequiredMixin, DetailView):
    model = AssemblyPost
    template_name = "PeoplePage/detail.html"
    context_object_name = "post"


class AnnoucementList(LoginRequiredMixin, ListView):
    model = AssemblyPost
    template_name = "AssemblyPage/Annoucemnts.html"
    context_object_name = "assembly"



    def get_queryset(self):
        return AssemblyPost.objects.filter(author=self.request.user)



class CreateAnnouncemts(LoginRequiredMixin, CreateView):
    form_class = CreateAnnouncementForm
    template_name = "AssemblyPage/create.html"
    success_url = reverse_lazy('post:Posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateAnnouncemts, self).form_valid(form)

class UpdateAnnouncements(LoginRequiredMixin, UpdateView):
    model = AssemblyPost
    template_name = "AssemblyPage/update.html"
    fields = ['title', 'description',  'main_image', 'supporting_image1', 'supporting_image2']
    success_url = reverse_lazy('post:announcements')

class AnnouncementDetail(LoginRequiredMixin, DetailView):
    model = AssemblyPost
    template_name = "PeoplePage/detail.html"
    context_object_name = "assemble"
"""
class People(LoginRequiredMixin, Create):
    model = Product
    template_name = 'sellers/details.html'
    context_object_name = "product"





class UpdateProduct(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "sellers/update.html"
    fields = ['name', 'image', 'description', 'category', 'price', 'available']


class DeleteProduct(LoginRequiredMixin, DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = "sellers/dlete.html"
    success_url = reverse_lazy('sellers:shop_list')


class OrderList(LoginRequiredMixin, ListView):
    model = OrderItem
    template_name = "sellers/orders.html"
    context_object_name = "orders"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders"] = context["orders"].filter(products__user=self.request.user)
        return context
"""
