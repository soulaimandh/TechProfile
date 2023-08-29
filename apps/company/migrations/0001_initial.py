# Generated by Django 4.2.4 on 2023-08-29 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("skills", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("company_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "company_name",
                    models.CharField(max_length=255, verbose_name="Nom d'entreprise"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Job",
            fields=[
                ("job_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "job_title",
                    models.CharField(max_length=255, verbose_name="Titre d'emploi"),
                ),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.company",
                        verbose_name="Entreprise",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RequiredSkill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.job",
                        verbose_name="Emploi",
                    ),
                ),
                (
                    "skill",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="skills.skill",
                        verbose_name="Compétence",
                    ),
                ),
            ],
            options={
                "verbose_name": "Compétence requise pour l'emploi",
                "verbose_name_plural": "Compétences requises pour les emplois",
            },
        ),
        migrations.CreateModel(
            name="CompanySubscription",
            fields=[
                (
                    "subscription_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "subscription_type",
                    models.CharField(max_length=255, verbose_name="Type d'abonnement"),
                ),
                ("start_date", models.DateField(verbose_name="Date de début")),
                ("end_date", models.DateField(null=True, verbose_name="Date de fin")),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.company",
                        verbose_name="Entreprise",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="requiredskill",
            constraint=models.UniqueConstraint(
                fields=("job", "skill"), name="unique_job_skill_"
            ),
        ),
    ]
