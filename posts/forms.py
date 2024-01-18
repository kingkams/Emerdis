from django import forms

from .models import PeoplePosts, AssemblyPost


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = PeoplePosts
        fields = ('problem', 'category', 'image')



class CreateAnnouncementForm(forms.ModelForm):
    class Meta:
        model = AssemblyPost
        fields = ('title', 'description', 'main_image', 'supporting_image1', 'supporting_image2')


