# Generated by Django 4.1.7 on 2023-04-01 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AttributeName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(default=None, max_length=100, null=True)),
                ('kod', models.CharField(default=None, max_length=30, null=True)),
                ('zobrazit', models.BooleanField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hodnota', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=255)),
                ('obrazek', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(default=None, max_length=255, null=True)),
                ('description', models.TextField(default=None, null=True)),
                ('cena', models.CharField(default=None, max_length=20, null=True)),
                ('mena', models.CharField(default=None, max_length=10, null=True)),
                ('published_on', models.DateTimeField(default=None, null=True)),
                ('is_published', models.BooleanField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=255)),
                ('obrazek_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='whys_app_data.image')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='whys_app_data.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='whys_app_data.attribute')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='whys_app_data.product')),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products_ids', models.ManyToManyField(to='whys_app_data.product')),
            ],
        ),
        migrations.AddField(
            model_name='attribute',
            name='hodnota_atributu_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='whys_app_data.attributevalue'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='nazev_atributu_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='whys_app_data.attributename'),
        ),
    ]