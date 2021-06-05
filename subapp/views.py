
from django.http import HttpResponse
from django.shortcuts import render
from subapp.models import Product, Brand
from subprocess import Popen, run, SubprocessError, PIPE
from django_client_framework.permissions import default_groups, add_perms_shortcut
from django.core.cache import cache

# Create your views here.
def clear(request):
    for cmd in [
        'python3 manage.py flush --no-input',
    ]: shell(cmd)
    # shell('python3 manage.py flush --no-input')
    cache.clear()
    add_perms_shortcut(default_groups.anyone, Product, "rwcd")
    add_perms_shortcut(default_groups.anyone, Brand, "rwcd")
    return HttpResponse('Successfully deleted all')

def shell(cmd, **kwargs):
    print(f"+ {cmd}", flush=True)
    return run(cmd, shell=True, text=True, check=True, **kwargs)