from django.http import HttpResponse
from django.urls import path
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from . import views

urlpatterns = [
    path('',views.homepage),

    path('yenileme-endpoint/', views.yenileme_endpoint, name='yenileme_endpoint'),

    path('login/', LoginView.as_view(), name='login'),

    path('company/',views.company,name='company'),
    path('company/s/<desc>',views.company_detail),

    path('view-excel/', views.view_excel, name='view_excel'),

    path('best-offer/', views.get_best_offer, name='get_best_offer'),

    path('statistic/',views.product_statistic,name = 'product_statistic'),

    path('offer/',views.offer,name="offer"),
    path('offer/s/<desc>',views.offer_detail),
    path('offer/c/<desc>',views.offer_change,name='offer_change'),
    path('offer/<int:offer_id>/delete/', views.delete_offer, name='delete_offer'),
    path('offer/c/<int:offer_id>/delete/<int:product_id>/', views.product_delete_from_offer, name='product_delete_from_offer'),

    ]

