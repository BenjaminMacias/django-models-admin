from django.urls import path

from ecommerce import views


urlpatterns = [
    path("", views.product_model_list_view, name="list"),
    path("<int:product_id>", views.product_model_detail_view, name="detail"),  #<------------ agregar model detail view
    path("create", views.product_model_create_view, name="create"), #<---agregar createview
    path("<int:product_id>/edit/", views.product_model_update_view, name="update"),
    path("<int:product_id>/delete/", views.product_model_delete_view, name="delete"),
  ]
