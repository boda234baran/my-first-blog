from django.contrib import admin
from .models import Post
#Щоб зробити нашу модель видимою на сторінці адміністратора, потрібно зареєструвати модель за допомогою admin.site.register(Post).
admin.site.register(Post)
