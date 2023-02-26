from home.views import listing_list,listing_retrieve
from django.urls import path
from . import views


urlpatterns = [
    path("", listing_list),
    path("listings/<pk>/", listing_retrieve),

]
