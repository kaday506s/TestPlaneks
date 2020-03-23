from django.contrib import admin
from apps.posts.models import Posts, Category, PostsComment

admin.site.register(Posts)
admin.site.register(Category)
admin.site.register(PostsComment)
