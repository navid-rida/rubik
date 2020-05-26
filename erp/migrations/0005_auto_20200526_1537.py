# Generated by Django 2.2.12 on 2020-05-26 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_auto_20200420_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='base_quantity',
            field=models.IntegerField(default=1, verbose_name='Base Quantity'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='body_page_material',
            field=models.CharField(default='N/A', max_length=100, verbose_name='Body Paper Material'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='coated_with',
            field=models.CharField(choices=[('ML', 'Matt Lamination'), ('MS', 'Matt & Spot Laminatio'), ('GL', 'Glossy Laminatio'), ('GE', 'Glue Lamination')], default='ML', max_length=2, verbose_name='Coated with'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='cover_color_number',
            field=models.IntegerField(default=1, verbose_name='Cover Number of Printer Colors'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='cover_page_material',
            field=models.CharField(default='N/A', max_length=100, verbose_name='Cover Paper Material'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='dye_cutting',
            field=models.BooleanField(default=True, verbose_name='Dye Cutting'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='increment_quantity',
            field=models.IntegerField(default=1, verbose_name='Increment Quantity'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='machine_height',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=3, verbose_name='Machine Height (in inch)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='machine_type',
            field=models.CharField(choices=[('ML', 'Matt Lamination'), ('MS', 'Matt & Spot Laminatio'), ('GL', 'Glossy Laminatio'), ('GE', 'Glue Lamination')], default='GTO', max_length=2, verbose_name='Machine Type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='machine_width',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=3, verbose_name='Machine Width (in inch)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='number_machine_master',
            field=models.IntegerField(default=1, verbose_name='Number of Machine / Master'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='number_pieces_master',
            field=models.IntegerField(default=1, verbose_name='Number of Pieces / Master'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='pages',
            field=models.IntegerField(default=1, verbose_name='Page / Book'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price_per_piece',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6, verbose_name='Base Price per piece (BDT)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price_per_piece_increment',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6, verbose_name='Increment per piece Price (rate after base quantity)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=4, verbose_name='Weight (kilogram)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Product Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='paper_material',
            field=models.CharField(max_length=100, verbose_name='Paper material'),
        ),
    ]
