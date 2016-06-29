from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
            # no text after the root URL means show list of posts 

        url(r'^post/(?P<post_id>\d+)/$', views.post_detail,
            name='post_detail'),
            # a URL starting with 'post/', followed by numbers, and then
            # again by a '/' would mean use the numbers to look up a
            # post ID and then render the details of that post.

        url(r'^post/new/$', views.post_new, name='post_new'),
            # a URL reading 'post/new/' means start a new post.

        url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit,
            name='post_edit'),
            # a URL starting with 'post/', followed by a number that is
            # the post ID, followed by an '/edit/' should redirect to
            # the correct post and open it in edit mode
        ]
