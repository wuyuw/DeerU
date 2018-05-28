# Generated by Django 2.0.3 on 2018-05-28 10:54

import app.ex_fields.fields
from django.db import migrations, models
import django.utils.timezone
import tool.kblog_model_field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='文件名')),
                ('img', models.ImageField(upload_to='', verbose_name='图片')),
            ],
            options={
                'verbose_name': '图片',
                'verbose_name_plural': '图片',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='标题')),
                ('summary', models.CharField(blank=True, editable=False, max_length=200, null=True, verbose_name='摘要')),
                ('image', models.CharField(blank=True, editable=False, max_length=200, null=True, verbose_name='图片')),
                ('content', app.ex_fields.fields.MFroalaField(verbose_name='正文')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.IntegerField(verbose_name='article_id')),
                ('category_id', models.IntegerField(verbose_name='分类id')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '文章分类',
                'verbose_name_plural': '文章分类',
            },
        ),
        migrations.CreateModel(
            name='ArticleMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.IntegerField(db_index=True, unique=True, verbose_name='article_id')),
                ('read_num', models.IntegerField(default=0, verbose_name='阅读量')),
                ('comment_num', models.IntegerField(default=0, verbose_name='评论量')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '文章meta',
                'verbose_name_plural': '文章meta',
            },
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.IntegerField(verbose_name='article_id')),
                ('tag_id', models.IntegerField(verbose_name='标签id')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='名称')),
                ('father_id', models.IntegerField(default=-1, verbose_name='父级目录')),
                ('m_order', models.PositiveIntegerField(default=0, verbose_name='排序')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'ordering': ['-m_order'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=20, null=True, verbose_name='昵称')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='邮箱')),
                ('content', models.TextField(verbose_name='内容')),
                ('article_id', models.IntegerField(verbose_name='article_id')),
                ('root_id', models.IntegerField(verbose_name='root_id')),
                ('to_id', models.IntegerField(default=-1, verbose_name='to_id')),
                ('type', models.IntegerField(choices=[(201, '对文章的评论'), (202, '对评论的评论')], verbose_name='type')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='配置名称')),
                ('config', app.ex_fields.fields.ConfigField(verbose_name='配置')),
                ('last_config', app.ex_fields.fields.ConfigField(blank=True, verbose_name='旧配置')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '配置',
                'verbose_name_plural': '配置',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='名称')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='UiConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='配置名称')),
                ('config', app.ex_fields.fields.ConfigField(verbose_name='配置')),
                ('last_config', app.ex_fields.fields.ConfigField(blank=True, verbose_name='旧配置')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '界面配置',
                'verbose_name_plural': '界面配置',
            },
        ),
    ]
