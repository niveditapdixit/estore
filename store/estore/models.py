from django.db import models

# Create your models here.
class Product(models.Model):
    productId = models.IntegerField(max_length = 20, primary_key=True)
    partNumber = models.CharField(max_length = 45)
    type = models.CharField(max_length = 45)
    inventory = models.IntegerField()
    salesRank = models.IntegerField(null=True)
    featured = models.CharField(max_length = 1, null=True, blank=True)
    
    def price(self):
        return self.priceSet.all()[0].price
    
    def description(self): 
        return self.productDescriptions.all()[0]
    
    def stock(self): 
        productRelation = ProductRelation.objects.get(parentProductId=self);
        product = productRelation.childProductId
        return product.inventory

    def __str__(self):
        return self.partNumber		
			
        
    class Meta:
        db_table = 'product'

class Category(models.Model):
    categoryId = models.IntegerField(max_length = 20, primary_key=True)
    categoryName = models.CharField(max_length = 45)
    displayName = models.CharField(max_length = 45)
    shortDescription = models.CharField(max_length = 45)
    longDescription = models.CharField(max_length = 45)    
    thumbNail = models.ImageField(upload_to='images/', null=True, blank=True) 
    fullImage = models.ImageField(upload_to='images/', null=True, blank=True)
    fullimagePath= models.CharField(max_length = 100)
    childCategories = models.ManyToManyField("self", through="CategoryXRef", symmetrical=False)
    childProducts = models.ManyToManyField(Product, through="CategoryChildProducts")
    def childCategoryNames(self):
        return ', '.join([category.categoryName for category in self.childCategories.all()])
    childCategoryNames.categoryName = "Categories Names"
    
    def __unicode__(self):
        return self.categoryName
		
    def __str__(self):
        return self.categoryName			
    
    class Meta:
        db_table = 'category'

class CategoryXRef(models.Model):
    parentCategory = models.ForeignKey(Category, db_column="parent", related_name="parentSet")
    childCategory = models.ForeignKey(Category, db_column="child", related_name="childSet")
    sequence = models.IntegerField(db_column="sequence")
    class Meta:
        db_table="categoryRelation"
        ordering=["sequence"]
        

class Price(models.Model):
    productId = models.ForeignKey('Product', db_column = "productId", primary_key=True,related_name="priceSet")
    partNumber = models.CharField(max_length = 45)
    price = models.FloatField()
    currency = models.CharField(max_length = 45)
	
    def __str__(self):
        return self.partNumber	
	
    class Meta:
        db_table = 'price'        
        
        
class ProductDescription(models.Model):
    productId = models.ForeignKey(Product, db_column = "productId", primary_key=True, related_name="productDescriptions")
    partNumber = models.CharField(max_length = 45)
    displayName = models.CharField(max_length = 45)
    shortDescription = models.CharField(max_length = 45)
    longDescription = models.CharField(max_length = 45)
    thumbNail = models.ImageField(upload_to='images/', null=True, blank=True)
    fullImage = models.ImageField(upload_to='estore/prodimages/', null=True, blank=True)
    fullimagePath= models.CharField(max_length = 100)	
    type = models.CharField(max_length = 45)

    def __str__(self):
        return self.partNumber		

    class Meta:
        db_table = 'productDescription'            
        
class ProductRelation(models.Model):
    parentProductId = models.ForeignKey(Product, db_column="parentProductId", related_name="parentProductSet")
    childProductId = models.ForeignKey(Product, db_column="childProductId", related_name="childProductIdSet")
    class Meta:
        db_table="productRelation"
        
class CategoryChildProducts(models.Model):
    categoryId = models.ForeignKey(Category, db_column="categoryId",related_name="childProductSet")
    childProductId = models.ForeignKey(Product, db_column="productId")
    partNumber = models.CharField(max_length = 45)
    def __str__(self):
        return self.partNumber	
    class Meta:
        db_table="categoryProductRelation"
		
class Customer(models.Model):
    customerId = models.IntegerField(max_length = 20, primary_key=True)
    firstName = models.CharField(max_length = 45)
    lastName = models.CharField(max_length = 45)
    shippingAddress = models.CharField(max_length = 1000)
    billingAddress = models.CharField(max_length = 1000, default="nivedita")
    addressline2 = models.CharField(max_length = 1000, default="nivedita")
    city = models.CharField(max_length = 45,  default="nivedita")
    country = models.CharField(max_length = 20,  default="nivedita")
    state = models.CharField(max_length = 20,  default="nivedita")	
    zipCode = models.CharField(max_length = 10,  default="nivedita")	
    homePhone = models.IntegerField(max_length=10 , default=12345)
    mobilePhone = models.IntegerField(max_length=10, default=12345)
    emailId =  models.CharField(max_length = 45 , default="nivedita@infosys.com")
    password = models.CharField(max_length = 45, default="Infy2015")
	

    def __str__(self):
        return self.firstName	
    class Meta:
        db_table="customer"  		
		
class Order(models.Model):
    orderId = models.IntegerField(max_length = 20, primary_key=True)
    totalPrice = models.FloatField()
    totalDiscount = models.FloatField()	
    totalTax = models.FloatField()	
    customer = models.ForeignKey(Customer, db_column = 'customerId', related_name='customerSet')
    class Meta:
        db_table="order"	
		
class OrderEntry(models.Model):
    orderId = models.ForeignKey(Order, db_column = 'orderId', related_name='orderSet')
    productId = models.IntegerField(max_length = 20)
    partNumber = models.CharField(max_length = 45)
    quantity = models.IntegerField(max_length = 20)
    totalPrice = models.FloatField()
    totalDiscount = models.FloatField()	
    totalTax = models.FloatField()	
    sequence = models.IntegerField(db_column="sequence")

    class Meta:
        db_table="orderEntry"			
	
  
	

