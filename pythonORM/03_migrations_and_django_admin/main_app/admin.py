from django.contrib import admin
from main_app.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Display the fields "name", "category", "price", and "created_on" (in that order) in the admin pane
    list_display = ('name', 'category', 'price', 'created_on')
    # Enable searching for "name", "category", and "supplier" fields
    search_fields = ('name', 'category', 'supplier')
    # Create filters for "category" and "supplier" fields
    list_filter = ['category','supplier']
    # Control the layout of "Add" and "Change" pages by grouping related fields within different sections:
    #  ◦ Group "General Information" with fields "name", "description", "price".
    #  ◦ Group "Categorization" with fields "category" and "supplier".
    fieldsets = (
        ('General Information', {'fields': ('name', 'description', 'price')}),
        ('Categorization', {'fields': ('category', 'supplier')}),
    )

    # Enable date-based drill-down navigation by the "created_on" field.
    date_hierarchy = 'created_on'