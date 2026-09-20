from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import TenantForm
from .models import Tenant


@login_required(login_url='login')
def create_tenant(request):
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            tenant = form.save()
            request.user.tenant = tenant
            request.user.is_admin = True
            request.user.is_customer = False
            request.user.save(update_fields=['tenant', 'is_admin', 'is_customer'])
            return redirect('task_list')
    else:
        form = TenantForm()
    return render(request, 'tenant/create.html', {'form': form})


@login_required(login_url='login')
def tenant_detail(request):
    tenant = request.user.tenant
    if tenant is None:
        return redirect('create_tenant')
    return render(request, 'tenant/detail.html', {'tenant': tenant})


@login_required(login_url='login')
def update_tenant(request,tenant_id):
    tenant = get_object_or_404(Tenant, id=tenant_id)
    if request.user.tenant_id != tenant.id or not request.user.is_admin:
        return redirect('tenant_detail')
    if request.method == 'POST':
        form = TenantForm(request.POST, instance=tenant)
        if form.is_valid():
            form.save()
            return redirect('tenant_detail')
    else:
        form = TenantForm(instance=tenant)
    return render(request, 'tenant/update.html', {'form': form, 'tenant': tenant})
