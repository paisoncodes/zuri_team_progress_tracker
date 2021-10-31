# Generated by Django 3.2.8 on 2021-10-29 18:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(default='Admin', max_length=100)),
                ('last_name', models.CharField(default='Admin', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('permissions', models.CharField(blank=True, choices=[('S', 'Staff'), ('A', 'Admin')], max_length=1)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('image', models.URLField(default='https://www.seekpng.com/ima/u2y3q8t4t4o0a9a9/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('about', models.TextField()),
                ('state', models.CharField(max_length=200)),
                ('batch', models.IntegerField(verbose_name='Year')),
                ('is_employed', models.BooleanField(default=False)),
                ('current_salary', models.IntegerField(default=0)),
                ('picture', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('subscriber_email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=800)),
                ('logo', models.URLField(default='https://ingressive.org/wp-content/uploads/2020/05/I4G-Logo-Color-Cropped.png')),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('male', models.IntegerField()),
                ('female', models.IntegerField()),
                ('year', models.IntegerField(unique=True)),
                ('finalist', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stack',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, unique_for_year='batch')),
                ('batch', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Stack',
                'verbose_name_plural': 'stacks',
                'unique_together': {('name', 'batch')},
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('job_title', models.CharField(max_length=255)),
                ('gotten_at', models.DateField()),
                ('company_name', models.CharField(max_length=255, verbose_name='Organization name')),
                ('job_description', models.CharField(max_length=255)),
                ('currently_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('job_logo', models.URLField(default='https://www.seekpng.com/ima/u2y3q8t4t4o0a9a9/')),
                ('intern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job', to='app.intern')),
            ],
        ),
        migrations.AddField(
            model_name='intern',
            name='stack',
            field=models.ManyToManyField(blank=True, related_name='intern_stack', to='app.Stack'),
        ),
    ]
