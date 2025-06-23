from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PerfilUsuarioForm
from .models import PerfilUsuario

@login_required
def perfil_usuario(request):
    user = request.user
    return render(request, 'cuentas/perfil_usuario.html', {'user': user})

@login_required
def editar_perfil(request):
    perfil, created = PerfilUsuario.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil_usuario')
    else:
        form = PerfilUsuarioForm(instance=perfil)

    return render(request, 'e-commerce/actualizar-usuario.html', {'form': form})