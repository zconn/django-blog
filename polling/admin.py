from django.contrib import admin

from django.contrib import admin
from polling.models import Poll
from blogging.models import Post, Category

admin.site.register(Poll)
#admin.site.register(Category)
