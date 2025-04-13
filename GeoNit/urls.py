from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('store/', include('shop.urls')),
    path('accounts/', include('accounts.urls')),
    path("planner/", include("planner.urls")),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)