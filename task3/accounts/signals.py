from django.db.models.signals import post_migrate, post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission, User
from .models import Profile
from project.models import Project


def get_permissions(perms_list):
    permissions = []
    for perm_str in perms_list:
        app_label, codename = perm_str.split('.')
        perm = Permission.objects.get(
            content_type__app_label=app_label,
            codename=codename
        )
        permissions.append(perm)
    return permissions


@receiver(post_migrate)
def CreateGroups(sender, **kwargs):
    print("start .......", sender)
    Admins, A_created = Group.objects.get_or_create(name='Admin')
    Manager, M_created = Group.objects.get_or_create(name='Manager')
    Developer, D_created = Group.objects.get_or_create(name='Developer')

    AdminsPerms = ['project.add_project', 'project.change_project',
                   'project.delete_project', 'project.view_project',
                   'accounts.change_profile', 'developers.change_developer',
                   'developers.view_developer']

    MangerPerms = ['project.add_project', 'project.change_project',
                   'project.view_project', 'accounts.view_profile',
                   'developers.view_developer']
    DeveloperPerms = ['accounts.view_profile',
                      'project.view_project', 'developers.view_developer']

    Admins.permissions.set(get_permissions(AdminsPerms))
    Admins.save()

    Manager.permissions.set(get_permissions(MangerPerms))
    Manager.save()

    Developer.permissions.set(get_permissions(DeveloperPerms))
    Developer.save()


@receiver(signal=post_save, sender=User)
def createProfile(sender, instance: User, **kwargs):
    Profile.objects.create(user=instance)
    devG = Group.objects.get(name="Developer")
    instance.groups.add(devG)


@receiver(signal=pre_save, sender=Project)
def addPrefix(sender, instance, **kwargs):
    instance.title = "**"+instance.title
