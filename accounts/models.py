from sys import maxsize
from django.contrib.auth.models import AbstractUser
from django.db import models


# class Role(models.Model):
#     name = models.CharField(maxsize=10)

role_choices = (('utilisateur', 'Utilisateur générique'),
                ('gestionaire', "Gestionaire d'école"),)

subrole_choices = (('admin', 'School Admin'),
                   ('editor', "School Editor"),)

# class SubRole(models.Model):
#     name = models.CharField(maxsize=10)


class CustomUser(AbstractUser):
    pass
    # role = models.ForeignKey(
    #     Role, on_delete=models.CASCADE, default=None)
    # subrole = models.ForeignKey(
    #     SubRole, on_delete=models.CASCADE, default=None)
    role = models.CharField(max_length=50, null=True, choices=role_choices)
    subrole = models.CharField(
        max_length=50, null=True, choices=subrole_choices)
    tel = models.CharField(max_length=20, null=True)
    photo = models.ImageField(
        upload_to='accounts/users', blank=True, null=True)
    # add additional fields in here

    def __str__(self):
        # return f'{self.username}(role: {self.role.name})(subrole: {self.subrole.name})'
        return f'{self.username}(role: {self.role})(subrole: {self.subrole})'
