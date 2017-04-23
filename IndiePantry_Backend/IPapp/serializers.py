###################################################################################
#   FILE NAME:   serializers.py
# 
# DESCRIPTION: In this file, serializers (objects that transfers database datatypes
#              into human-readable JSON) are defined for at least each table in the
#              database.  Each class in serializers.py corresponds to a ViewSet in
#              views.py.
#
# REFERENCES:  views.py, models.py
#
#    DATE        BY      DESCRIPTION
# ==========  ========  ===============
#  04/06/17   Layne H.  Created serializer for the Vendor database table.
#  04/07/17   Layne H.  Created serializer for the Customer, MenuCategory, MenuItem,
#                       Sale, Review, ReviewFlag, and Advertising database tables.
#
####################################################################################

from .models import *
from rest_framework import serializers

class VendorSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = Vendor
                fields = ('vendorAddress', 'emailV', 'passwordV', 'phone', 'rating', 'nameV', 'approved')
 
class CustomerSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = Customer
                fields = ('username', 'passwordC', 'nameC', 'customerAddress', 'emailC')
 
class MenuCategorySerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = MenuCategory
                fields = ('category','size','vendor_fmenucategory')
 
class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = MenuItem
                fields = ('cost', 'iType', 'description', 'menu_fmenuitem')
 
class SaleSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = Sale
                fields = ('date', 'total', 'tax', 'customer_fsale', 'item_fsale', 'menu_fsale', 'vendor_fsale')
 
class ReviewSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = Review
                fields = ('text', 'rate', 'customer_freview', 'vendor_freview')
 
class ReviewFlagSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = ReviewFlag
                fields = ('reason', 'review_freviewflag')
 
class AdvertisingSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = Advertising
                fields = ('start', 'vendor_fadvertising')