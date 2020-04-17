"""djancomarea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from engine import views
# from tutorial
from django.conf.urls import include
#
# В качестве альтернативы для определения маршрутов мы можем использовать функцию re_path()
urlpatterns = [
    # from tutorial
    path('palata/', include('engine.urls')),
    #
    re_path(r'^ip', views.nahui), # регулярки. пригодится для доступа к отдельным комнатам
    #re_path(r'^palata#(?P<chatid>[\d\w]+)', views.unauthorized, name='unauthorized'),
    # возможно, будем потом пускать в чат, предварительно зарегистрировав рандомное имя
    # я так подумал. а давайте!
    re_path(r'paradnoe', views.paradnoe, name='paradnoe'),
    path('admin/', admin.site.urls),
    path('', views.index),

]
# Когда запрос приходит к приложению, то система проверяет соответствие запроса маршрутам
# по мере их определения: вначале сравнивается первый маршрут, если он не подходит,
# то сравнивается второй и так далее. Поэтому более общие маршруты должны определяться
# в последнюю очередь, а более конкретные маршруты должны идти в начале.
