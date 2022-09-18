from django.contrib import admin
from django.urls import path, include
from userinfo.views import HomeView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    # userinform urls.
    path('portfolio/', include('userinfo.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ADMIN PANEL HEADER AND TITLE TEXT CHANGE.
admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin Portal"
admin.site.index_title = "Welcome to Portfolio Portal"