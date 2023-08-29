from django.db import models

# Create your models here.
# Modèles de compétences
class Skill(models.Model):
    skill_id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=255, verbose_name="Nom de compétence")

class SkillTest(models.Model):
    test_id = models.AutoField(primary_key=True)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, verbose_name="Compétence")

class TestQuestion(models.Model):
    question_id = models.AutoField(primary_key=True)
    test = models.ForeignKey(SkillTest, on_delete=models.CASCADE, verbose_name="Test")
    question_text = models.TextField(verbose_name="question")
    correct_answer = models.CharField(max_length=255, verbose_name="Réponse correcte")

