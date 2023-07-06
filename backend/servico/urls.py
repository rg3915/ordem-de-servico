from django.urls import path

from backend.servico import views as v

app_name = 'servico'


urlpatterns = [
    path('', v.ordem_servico_list, name='ordem_servico_list'),  # noqa E501
    path('create/', v.ordem_servico_create, name='ordem_servico_create'),  # noqa E501
    path('<int:pk>/', v.ordem_servico_detail, name='ordem_servico_detail'),  # noqa E501
    path('<int:pk>/update/', v.ordem_servico_update, name='ordem_servico_update'),  # noqa E501
    # path('<int:pk>/delete/', v.ordem_servico_delete, name='ordem_servico_delete'),  # noqa E501
]
