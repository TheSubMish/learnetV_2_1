from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from learnetV_2_1.settings import STATIC_URL,STATICFILES_DIRS,MEDIA_URL,MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('userlog.urls')),
    path('student/',include('student.urls')),
    path('teacher/',include('teacher.urls')),
    path('course/',include('course.urls')),
]

urlpatterns += static(STATIC_URL,document_root=STATICFILES_DIRS)
urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)