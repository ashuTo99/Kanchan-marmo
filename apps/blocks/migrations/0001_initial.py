# Generated by Django 4.2.1 on 2023-06-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_number', models.BigIntegerField(unique=True)),
                ('varient', models.CharField(blank=True, max_length=300, null=True)),
                ('bench_number', models.BigIntegerField(blank=True, null=True)),
                ('name_of_person', models.CharField(blank=True, max_length=300, null=True)),
                ('block_picture', models.ImageField(blank=True, null=True, upload_to='uploads/block')),
                ('block_length', models.FloatField()),
                ('block_height', models.FloatField()),
                ('block_weight', models.FloatField()),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'blocks',
            },
        ),
    ]
