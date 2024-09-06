# Generated by Django 4.2 on 2024-09-03 09:19

from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, default='category.jpg', null=True, upload_to='category')),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.FileField(blank=True, default='product.jpg', null=True, upload_to='products')),
                ('description', models.TextField(blank=True, null=True)),
                ('tags', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('shipping_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('stock_qty', models.PositiveIntegerField(default=0)),
                ('in_stock', models.BooleanField(default=True)),
                ('status', models.CharField(blank=True, choices=[('draft', 'Draft'), ('disabled', 'Disabled'), ('rejected', 'Rejected'), ('in_review', 'In Review'), ('published', 'Published')], default='published', max_length=50, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('views', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('rating', models.IntegerField(blank=True, default=0, null=True)),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=20, prefix='', unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='store.category')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendor', to='vendor.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.CharField(blank=True, max_length=1000, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=2, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default='product.jpg', upload_to='products')),
                ('active', models.BooleanField(default=True)),
                ('gid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=25, prefix='')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('color_code', models.CharField(blank=True, max_length=1000, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]