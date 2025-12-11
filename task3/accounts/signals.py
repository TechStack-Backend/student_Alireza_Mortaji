from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission


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
                   'project.delete_project', 'project.view_project', 'accounts.change_profile']
    MangerPerms = ['project.add_project', 'project.change_project',
                   'project.view_project', 'accounts.view_profile']
    DeveloperPerms = ['accounts.view_profile', 'project.view_project']

    if A_created:
        Admins.permissions.set(get_permissions(AdminsPerms))
        Admins.save()
        print("done1")

    if M_created:
        Manager.permissions.set(get_permissions(MangerPerms))
        Manager.save()
        print("done2")

    if D_created:
        Developer.permissions.set(get_permissions(DeveloperPerms))
        Developer.save()
        print("done 3")
