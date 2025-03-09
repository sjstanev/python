from django.db import migrations, models
import random

def add_barcode_data(apps, schema_editor):
    Product = apps.get_model("main_app", "Product")
    used_barcodes = set(Product.objects.values_list("barcode", flat=True))

    for product in Product.objects.all():
        barcode = random.randint(100000, 999999)
        while barcode in used_barcodes:  # Ensure uniqueness
            barcode = random.randint(100000, 999999)

        product.barcode = barcode
        used_barcodes.add(barcode)
        product.save()

def reverse_add_barcode(apps, schema_editor):
    Product = apps.get_model("main_app", "Product")
    Product.objects.update(barcode=None)  # Reset barcodes

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_product_category_alter_product_supplier'),  # Update if needed
    ]

    operations = [
        # ✅ Step 1: Add the new column
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        # ✅ Step 2: Populate the column with data
        migrations.RunPython(add_barcode_data, reverse_add_barcode),
    ]
