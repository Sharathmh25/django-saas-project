from django.urls import path
from .views import create_tenant,tenant_detail,update_tenant
urlpatterns=[
       path('create/', create_tenant, name='create_tenant'),
       path('detail/', tenant_detail, name='tenant_detail'),
       path('update/<int:tenant_id>/', update_tenant, name='update_tenant')
]