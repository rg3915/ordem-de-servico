from django.urls import path

from backend.crm import views as v

app_name = 'crm'


urlpatterns = [
    path('', v.ClienteListView.as_view(), name='cliente_list'),  # noqa E501
    path('create/', v.ClienteCreateView.as_view(), name='cliente_create'),  # noqa E501
    path('<int:pk>/', v.ClienteDetailView.as_view(), name='cliente_detail'),  # noqa E501
    path('<int:pk>/update/', v.ClienteUpdateView.as_view(), name='cliente_update'),  # noqa E501
    # path('<int:pk>/delete/', v.ClienteDeleteView.as_view(), name='cliente_delete'),  # noqa E501
]
