# Generated by Django 2.2.11 on 2021-01-25 14:54

from django.db import migrations, connection


def forward(apps, schema_editor):
    DateField = apps.get_model('database', 'DateField')

    with connection.schema_editor() as tables_schema_editor:
        # We need to stop the transaction because we might need to lock a lot of tables
        # which could result in an out of memory exception.
        tables_schema_editor.atomic.__exit__(None, None, None)

        for field in DateField.objects.all():
            table_name = f'database_table_{field.table.id}'
            field_name = f'field_{field.id}'
            tables_schema_editor.execute(
                f"""
                    UPDATE {table_name} SET {field_name} = '0001-01-01'::date
                    WHERE {field_name} < '0001-01-01'::date
                """
            )


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0027_gridviewfieldoptions_order'),
    ]

    operations = [
        migrations.RunPython(forward, migrations.RunPython.noop),
    ]
