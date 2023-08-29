from django.db import models

from param.models import CustomUser
from apps.company.models import Job
from apps.skills.models import Skill, SkillTest

# Create your models here.
# Modèles de candidat
class Candidate(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=255, verbose_name="Nom complet")
    date_of_birth = models.DateField(null=True, verbose_name="Date de naissance")
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)

class CandidateCV(models.Model):
    cv_id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, verbose_name="Candidat")
    address = models.TextField(null=True, verbose_name="Adresse")
    phone_number = models.CharField(max_length=255, null=True, verbose_name="Numéro de téléphone")
    projects = models.TextField(null=True, verbose_name="Projets")
    languages = models.TextField(null=True, verbose_name="Langues")
    summary = models.TextField(null=True, verbose_name="Résumé")

class CVExperience(models.Model):
    cv = models.ForeignKey(CandidateCV, on_delete=models.CASCADE)
    position = models.CharField(max_length=255, verbose_name="Poste")
    company = models.CharField(max_length=255, verbose_name="Entreprise")
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(null=True, verbose_name="Date de fin")
    description = models.TextField(verbose_name="Description")

class CVEducation(models.Model):
    cv = models.ForeignKey(CandidateCV, on_delete=models.CASCADE)
    institution = models.CharField(max_length=255, verbose_name="Institution")
    degree = models.CharField(max_length=255, verbose_name="Diplôme")
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(null=True, verbose_name="Date de fin")

class CandidateSkill(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, verbose_name="Candidat")
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, verbose_name="Compétence")
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['candidate', 'skill'], name='unique_candidate_skill_')
        ]
        verbose_name = "Compétence du candidat"

class CandidateRanking(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, verbose_name="Candidat")
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, verbose_name="Compétence")
    ranking = models.IntegerField(verbose_name="Classement")

class CandidateApplication(models.Model):
    APPLICATION_STATUS_CHOICES = (
        ('Submitted', 'Submitted'),
        ('Reviewed', 'Reviewed'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )
    application_id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, verbose_name="Candidat")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="Emploi")
    application_date = models.DateTimeField(auto_now_add=True, verbose_name="Date de candidature")
    status = models.CharField(max_length=255, choices=APPLICATION_STATUS_CHOICES, verbose_name="Statut")
    
    def __str__(self):
        return f"{self.candidate.username} - {self.job.job_title} - {self.get_status_display()}"

class TestSubmission(models.Model):
    submission_id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, verbose_name="Candidat")
    test = models.ForeignKey(SkillTest, on_delete=models.CASCADE)
    submission_timestamp = models.DateTimeField(auto_now_add=True)
    models.DateTimeField(auto_now_add=True)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    ranking = models.IntegerField(verbose_name="Classement")