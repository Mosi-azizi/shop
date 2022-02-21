from django.urls import path

from shop_order.views import add_user_order,user_open_order,send_request,verify,remove_order_detail

urlpatterns = [
    path('add-user-order', add_user_order),
    path('open-order',user_open_order),
    path('remove-order-detail/<detail_id>',remove_order_detail),
    path('pay',send_request,name='request'),
    path('verify/<order_id>',verify,name='verify')

]