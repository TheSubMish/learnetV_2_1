# Generated by Django 4.2.5 on 2024-01-19 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('district', models.CharField(max_length=30, null=True)),
                ('state', models.CharField(max_length=30, null=True)),
                ('edubackground', models.CharField(choices=[('1', 'Higher Secondary'), ('2', 'Diploma or Certificate Programs'), ('3', "Bachelor's Degree"), ('4', "Master's Degree"), ('5', 'Doctoral Degree (Ph.D.)')], default='1', max_length=30, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html', models.BooleanField(default=False, null=True)),
                ('css', models.BooleanField(default=False, null=True)),
                ('javascript', models.BooleanField(default=False, null=True)),
                ('python', models.BooleanField(default=False, null=True)),
                ('data_analysis', models.BooleanField(default=False, null=True)),
                ('data_structure_and_algorithms', models.BooleanField(default=False, null=True)),
                ('natural_language_processing', models.BooleanField(default=False, null=True)),
                ('machine_learning', models.BooleanField(default=False, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.test')),
            ],
        ),
    ]
