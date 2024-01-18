from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PeoplelistView, AnnoucementView, CreatePost, DeletePost, AssemblyList, AnnoucementList, \
    CreateAnnouncemts, \
    UpdateAnnouncements, DeleteAnnouncement, AnnouncementDetail

app_name = 'post'

urlpatterns = [
    path('', PeoplelistView.as_view(), name='Posts'),
    path('Anoucements/posts', AnnoucementView.as_view(), name='alerts'),
    path('Anoucements/', AnnoucementList.as_view(), name='announcements'),
    path('<str:pk>/Anoucements/detail', AnnouncementDetail.as_view(), name='detail'),
    path('create_task/', CreatePost.as_view(), name='create_view'),
    path('<str:pk>/Delete/', DeletePost.as_view(), name='delete_post'),
    path('<str:pk>/assembly/update', UpdateAnnouncements.as_view(), name='update'),
    path('<str:pk>/Delete_anouncement/', DeleteAnnouncement.as_view(), name='delete'),
    path('assembly', AssemblyList.as_view(), name='AssemPost'),
    path('create_announcement/', CreateAnnouncemts.as_view(), name='create_Announcemt'),

]
