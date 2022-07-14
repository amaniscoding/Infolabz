# Generated by Django 4.0.5 on 2022-06-25 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0002_rename_prodct_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('Quantity', models.IntegerField()),
                ('description', models.CharField(max_length=150)),
                ('categoryname', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='internship.category')),
            ],
        ),
    ]