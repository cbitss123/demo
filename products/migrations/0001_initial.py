# Generated by Django 3.1.6 on 2021-06-17 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('img', models.ImageField(blank=True, upload_to='pics')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
                ('desc1', models.TextField()),
                ('desc2', models.TextField()),
                ('specialOffer', models.BooleanField(default=False)),
                ('producturl', models.URLField(max_length=40)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
    ]
