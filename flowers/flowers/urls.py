from django.contrib import admin
from django.urls import path,include
from flower import views
from about_us import views as v
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from authentication1.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/flowers/', views.flower_list, name="flowers_list"),
    path('home/about_us',v.about_view),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('home/', home_view, name='home'),
    path("accounts/", include("django.contrib.auth.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


