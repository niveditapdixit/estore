from django.conf.urls import patterns, url

from estore import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^prodimages/(?P<product_id>\d+)\.jpg$', views.getProductImage, name="getProductImage"),
    url(r'^categories.json/(?P<category_id>\d+)$', views.getJSONCategory, name="getJSONCategory"),
    url(r'^categories.json', views.getJSONCategories, name="getJSONCategories"),
    url(r'^products.json/(?P<product_id>\d+)$', views.getJSONProduct, name="getJSONProduct"),
    url(r'c/.+/(?P<categoryId>\d+)$',views.productListing, name='productListing'),
    url(r'p/.+/(?P<productId>\d+)$',views.productDetail, name='productDetail'),
	url(r'^register$',views.register, name='register'),
    url(r'^login$', views.login,name='login'),
    url(r'^logout$', views.logout,name='logout'),	
)