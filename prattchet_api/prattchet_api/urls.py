from django.contrib import admin
from django.urls import include, path

from quotes.views import QuoteViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('quotes', QuoteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
