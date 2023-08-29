from django.db import models

from apps.skills.models import Skill

# Create your models here.
# Modèles d'entreprise
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255, verbose_name="Nom d'entreprise")

class CompanySubscription(models.Model):
    subscription_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Entreprise")
    subscription_type = models.CharField(max_length=255, verbose_name="Type d'abonnement")
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(null=True, verbose_name="Date de fin")

# Modèles d'emploi
class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Entreprise")
    job_title = models.CharField(max_length=255, verbose_name="Titre d'emploi")
    description = models.TextField(verbose_name="Description")

class RequiredSkill(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="Emploi")
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, verbose_name="Compétence")
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['job', 'skill'], name='unique_job_skill_')
        ]
        verbose_name = "Compétence requise pour l'emploi"
        verbose_name_plural = "Compétences requises pour les emplois"
