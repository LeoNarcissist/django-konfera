# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 21:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountCodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('hash', models.CharField(max_length=64)),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('available_from', models.DateTimeField()),
                ('available_to', models.DateTimeField()),
                ('usage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField()),
                ('event_type', models.CharField(choices=[('conference', 'Conference'), ('meetup', 'Meetup')], max_length=20)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('expired', 'Expired')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('street', models.CharField(max_length=128)),
                ('street2', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('postcode', models.CharField(max_length=12)),
                ('state', models.CharField(max_length=128)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.CharField(choices=[('awaiting_payment', 'Awaiting payment'), ('paid', 'Paid'), ('expired', 'Expired'), ('cancelled', 'Cancelled')], max_length=256)),
                ('purchase_date', models.DateTimeField()),
                ('payment_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('street', models.CharField(max_length=128)),
                ('street2', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('postcode', models.CharField(max_length=12)),
                ('state', models.CharField(max_length=128)),
                ('companyid', models.CharField(max_length=32)),
                ('taxid', models.CharField(max_length=32)),
                ('vatid', models.CharField(max_length=32)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('description', models.CharField(max_length=128)),
                ('duration', models.IntegerField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='konfera.Room')),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('title', models.CharField(choices=[('none', ''), ('mr', 'Mr.'), ('ms', 'Ms.')], default='none', max_length=4)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=64)),
                ('bio', models.TextField()),
                ('url', models.URLField()),
                ('social_url', models.URLField()),
                ('country', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('type', models.CharField(choices=[('platinum', 'Platinum'), ('gold', 'Gold'), ('silver', 'Silver'), ('bronze', 'Bronze'), ('other', 'Other'), ('django_girls', 'Django girls')], max_length=32)),
                ('logo', models.FileField(upload_to='')),
                ('url', models.URLField()),
                ('about_us', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('abstract', models.TextField()),
                ('type', models.CharField(choices=[('talk', 'Talk'), ('workshop', 'Workshop')], max_length=32)),
                ('status', models.CharField(choices=[('cfp', 'Call For Proposals'), ('draft', 'Draft'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('withdrawn', 'Withdrawn')], max_length=32)),
                ('duration', models.CharField(choices=[(5, '5 min'), (30, '30 min'), (45, '45 min')], max_length=32)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='konfera.Event')),
                ('primary_speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondary_speaker', to='konfera.Speaker')),
                ('secondary_speaker', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='primary_speaker', to='konfera.Speaker')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('requested', 'Requested'), ('registered', 'Registered'), ('checked-in', 'Checked-in'), ('cancelled', 'Cancelled')], max_length=32)),
                ('title', models.CharField(choices=[('none', ''), ('mr', 'Mr.'), ('ms', 'Ms.')], default='none', max_length=4)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('discount_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='konfera.DiscountCodes')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='konfera.Order')),
            ],
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('available_from', models.DateTimeField()),
                ('available_to', models.DateTimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='konfera.Event')),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='konfera.TicketType'),
        ),
        migrations.AddField(
            model_name='speaker',
            name='sponsor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='konfera.Sponsor'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='talk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='konfera.Talk'),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='konfera.Location'),
        ),
        migrations.AddField(
            model_name='event',
            name='sponsors',
            field=models.ManyToManyField(blank=True, related_name='sponsored_events', to='konfera.Sponsor'),
        ),
        migrations.AddField(
            model_name='discountcodes',
            name='ticket_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='konfera.TicketType'),
        ),
    ]
