from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): # наслідуючи від medels.Model django добавить обєкт в базу
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)# ссилка на іншу модель
    title = models.CharField(max_length=200)#ЗАГОЛОВОК,  оприділили текстове поле з обмеженою кількістю символів (тут 200)
    text = models.TextField()#оприділяється поле для необмеженої кіллькості символів
    created_date = models.DateTimeField(default=timezone.now) # дата і час
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): #(функція = метод) метод публікації для записі
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
