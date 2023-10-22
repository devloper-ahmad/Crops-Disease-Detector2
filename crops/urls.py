"""crops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path,include
from crops import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', views.index,name='index'),
    path('account/',views.account,name='account'),
    path('doctor/',views.doctor, name='doctor'),
    path('Amistar/<Amistarid>',views.Amistar, name='Amistar'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('Medicine2/',views.Medicine2, name='Medicine2'),
    path('order1/',views.order1, name='order1'),
    path('changepassword/',views.change_password, name='changepassword'),
    path('diseasedetail/<diseaseid>',views.diseasedetail,name='diseasedetail'),
    path('Researchdetail/<Researchid>',views.Researchdetail,name='Researchdetail'),
    path('Researchuploader/',views.Researchuploader,name='Researchuploader'),
    path('Research1/',views.Research1,name='Research1'),
    path('About1/<Aboutid>',views.About1,name='About1'),
    path('detect/<detectid>',views.detect,name='detect'),
    path('detect1/<detect1id>',views.detect1,name='detect1'),
    path('video/',views.video,name='video'),
    path("predict_image/", include("predict.urls")),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)