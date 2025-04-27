from django.shortcuts import render, redirect, get_object_or_404
from .models import Eleve
from django.contrib import messages  

def liste_eleves(request):
    if request.method == 'POST':
        id_eleve = request.POST.get('id_eleve')
        if id_eleve:
            # Si ID existe => Modifier
            eleve = get_object_or_404(Eleve, id=id_eleve)
        else:
            # Sinon => Créer un nouveau
            eleve = Eleve()

        eleve.prenom = request.POST['prenom']
        eleve.nom = request.POST['nom']
        eleve.age = request.POST['age']
        eleve.note_francais = request.POST['note_francais']
        eleve.note_anglais = request.POST['note_anglais']
        eleve.note_math = request.POST['note_math']
        eleve.save()
        return redirect('liste_eleves')

    eleves = Eleve.objects.all()
    return render(request, 'app_eleves/liste.html', {'eleves': eleves})


def ajouter_modifier_eleve(request):
    id_eleve = request.GET.get('id')  # on récupère l'ID dans l'URL si on modifie
    eleve = None

    if id_eleve:
        eleve = get_object_or_404(Eleve, id=id_eleve)

    if request.method == 'POST':
        prenom = request.POST.get('prenom')
        nom = request.POST.get('nom')
        age = request.POST.get('age')
        note_francais = request.POST.get('note_francais')
        note_anglais = request.POST.get('note_anglais')
        note_math = request.POST.get('note_math')

        if request.POST.get('id_eleve'):  # si ID existe → modification
            eleve = get_object_or_404(Eleve, id=request.POST.get('id_eleve'))
            eleve.prenom = prenom
            eleve.nom = nom
            eleve.age = age
            eleve.note_francais = note_francais
            eleve.note_anglais = note_anglais
            eleve.note_math = note_math
            eleve.save()
        else:  # sinon création
            Eleve.objects.create(
                prenom=prenom,
                nom=nom,
                age=age,
                note_francais=note_francais,
                note_anglais=note_anglais,
                note_math=note_math
            )
        # Message de succès après l'ajout de l'élève
        messages.success(request, f"L'élève {prenom} {nom} a été ajouté avec succès !")
        return redirect('app_eleves:liste_eleves')

    eleves = Eleve.objects.all()
    return render(request, 'app_eleves/liste.html', {'eleves': eleves, 'eleve': eleve})


def detail_eleve(request, id):
    eleve = get_object_or_404(Eleve, id=id)
    return render(request, 'app_eleves/details.html', {'eleve': eleve})

def supprimer_eleve(request, id):
    eleve = get_object_or_404(Eleve, id=id)
    eleve.delete()
    return redirect('app_eleves:liste_eleves')

def modifier_eleve(request, id):
    eleve = get_object_or_404(Eleve, id=id)

    if request.method == 'POST':
        eleve.prenom = request.POST.get('prenom')
        eleve.nom = request.POST.get('nom')
        eleve.age = request.POST.get('age')
        eleve.note_francais = request.POST.get('note_francais')
        eleve.note_anglais = request.POST.get('note_anglais')
        eleve.note_math = request.POST.get('note_math')
        eleve.save()
        # Message de succès après l'ajout de l'élève
        messages.success(request, f"Modification effectuée avec succès !")
        return redirect('app_eleves:liste_eleves')

    return render(request, 'app_eleves/modifier.html', {'eleve': eleve})


