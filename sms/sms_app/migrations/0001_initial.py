# Generated by Django 5.0.2 on 2024-03-02 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cls_grade', models.CharField(max_length=150)),
                ('cls_section', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('contact_email', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subj_name', models.CharField(max_length=30)),
                ('subj_duration', models.IntegerField()),
                ('cls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cls_subj', to='sms_app.cls')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('grade', models.CharField(max_length=150)),
                ('cls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cls_enrol', to='sms_app.cls')),
                ('Subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects_taught', to='sms_app.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assign_name', models.CharField(max_length=150)),
                ('assign_percentage', models.CharField(max_length=150)),
                ('assignment_subj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assess_subj_name', to='sms_app.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Assesment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ass_name', models.CharField(max_length=150)),
                ('ass_percentage', models.CharField(max_length=150)),
                ('assessment_subj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ass_subj_name', to='sms_app.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('edu_level', models.CharField(max_length=150)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_list', to='sms_app.department')),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules_taught', to='sms_app.teacher'),
        ),
    ]
