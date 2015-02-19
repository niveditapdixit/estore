from django.contrib import admin

# Register your models here.
from estore.models import Category, CategoryXRef, Product,Price,ProductDescription,ProductRelation,CategoryChildProducts, Customer, Order, OrderEntry

class CategoryChildProductInline(admin.TabularInline):
    model = CategoryChildProducts
    fk_name = 'categoryId'
    extra = 1 
class CategoryXRefInline(admin.TabularInline):
    model = CategoryXRef
    fk_name = 'parentCategory'
    extra = 1     
class CategoryAdmin(admin.ModelAdmin):
    inlines = (CategoryXRefInline,CategoryChildProductInline)
    list_display = ('categoryId', 'categoryName','childCategoryNames')
    fieldsets = [
        (None,               {'fields': ['categoryId']}),
        ('categoryName', {'fields': ['categoryName'], 'classes': ['collapse']}),
        ('displayName', {'fields': ['displayName']}),
        ('shortDescription', {'fields': ['shortDescription']}),
        ('longDescription', {'fields': ['longDescription']}),
		('thumbNail' ,               {'fields': ['thumbNail']}),
        ('fullImage', {'fields': ['fullImage']}),
    ]
    search_fields = ('categoryId', 'categoryName')
    list_filter = ('categoryId', 'categoryName')
    ordering = ('categoryId',)
    #filter_horizontal = ('childCategoryNames',)
#   inlines = [CategoryXRefInline]
class CategoryXRefAdmin(admin.ModelAdmin):
    list_display = ('parentCategoryName', 'childCategoryName','sequence')
    search_fields = ('parentCategoryName', 'childCategoryName', 'sequence')    
    #list_editable = ('parentCategoryName', 'childCategoryName','sequence')
    
    def parentCategoryName(self, instance):
        return instance.parentCategory.categoryName    
    def childCategoryName(self, instance):
        return instance.childCategory.categoryName            
    pass    
class ProductDescriptionInline(admin.TabularInline):
    model = ProductDescription
    extra = 1 
    
class PriceInline(admin.TabularInline):
    model = Price
    extra = 1
        
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductDescriptionInline,PriceInline)
    list_display = ('productId', 'partNumber')
    search_fields = ('productId', 'partNumber')    
    list_filter = ('productId', 'partNumber')    
    pass
class ProductDescriptionAdmin(admin.ModelAdmin):
    list_display = ('productId', 'partNumber','shortDescription')
    search_fields = ('productId', 'partNumber','shortDescription')        
    list_filter = ('productId', 'partNumber','shortDescription')        
    pass
class PriceAdmin(admin.ModelAdmin):
    list_display = ('productId', 'price','currency')
    search_fields = ('productId', 'price','currency')            
    list_filter = ('productId', 'price','currency')            
    pass
class ProductRelationAdmin(admin.ModelAdmin):
    list_display = ('parentProductId', 'childProductId')
    search_fields = ('parentProductId', 'childProductId')                
    pass
class CategoryChildProductAdmin(admin.ModelAdmin):
    list_display = ('parentCategoryName', 'childProductName', 'partNumber')
    search_fields = ('categoryId', 'childProductId','partNumber')                
    def parentCategoryName(self, instance):
        return instance.categoryId
    def childProductName(self, instance):
        return instance.childProductId                
    pass    

admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryXRef, CategoryXRefAdmin)        
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductDescription, ProductDescriptionAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(ProductRelation, ProductRelationAdmin)
admin.site.register(CategoryChildProducts, CategoryChildProductAdmin)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(OrderEntry)
