from django.urls import path
from Twood import views

urlpatterns=[
	# path('',views.apioverview,name="apioverview"),
	path('product-list/',views.Showall,name='product-list'),
	path('product-view/<int:pk>/',views.ViewProduct,name='product-view'),
	path('product-create/',views.CreateProduct,name='product-create'),
	path('product-update/<int:pk>/',views.UpdateProduct,name='product-update'),
	path('product-delete/<int:pk>/',views.DeleteProduct,name='product-delete'),

]