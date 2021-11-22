# Generated by Django 3.2.9 on 2021-11-18 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Blog_title', models.CharField(max_length=30)),
                ('Blog_catogery', models.CharField(choices=[('python', 'Python'), ('C++', 'C++'), ('Java', 'Java'), ('JavaScript', 'JavaScript'), ('Php', 'Php'), ('C', 'C')], max_length=30)),
                ('Blog_desc', models.TextField(max_length=100)),
                ('Blog_detail_desc', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('Country', models.CharField(max_length=20)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='USER_Data',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
    ]
