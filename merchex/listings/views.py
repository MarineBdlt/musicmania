from typing import List
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect

from listings.forms import BandForm, ListingForm


def band_list(request):
    bands = Band.objects.all()
    return render(
        request, "listings/band_list.html", {"bands": bands}
    )  # reponse, chemin pour accéder au template, dictionnaire de contexte


def band_detail(request, id):
    band = Band.objects.get(id=id)  # notez le paramètre id supplémentaire
    return render(
        request, "listings/band_detail.html", {"band": band}
    )  # nous passons l'id au modèle


def about(request):
    return render(request, "listings/about.html")


def listing_list(request):
    listings = Listing.objects.all()
    return render(request, "listings/listing_list.html", {"listings": listings})


def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request, "listings/listing_detail.html", {"listing": listing})


def contact(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=["admin@merchex.xyz"],
            )
        return redirect("email-sent")
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
    else:
        form = ContactUsForm()
    return render(request, "listings/contact.html", {"form": form})


def email_sent(request):
    return render(request, "listings/email_sent.html")


def band_create(request):
    if request.method == "POST":
        form = BandForm(request.POST, request.FILES)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save(commit=False)
            print(band)
            band.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect("band-detail", band.id)

    else:
        form = BandForm()

    return render(request, "listings/band_create.html", {"form": form})


# @login_required
# def photo_upload(request):
#     form = forms.PhotoForm()
#     if request.method == 'POST':
#         form = forms.PhotoForm(request.POST, request.FILES)
#         if form.is_valid():
#             photo = form.save(commit=False)
#             # set the uploader to the user before saving the model
#             photo.uploader = request.user
#             # now we can save
#             photo.save()
#             return redirect('home')
#     return render(request, 'blog/photo_upload.html', context={'form': form})


def listing_create(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            listing = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect("listing-detail", listing.id)

    else:
        form = ListingForm()

    return render(request, "listings/listing_create.html", {"form": form})


def band_change(request, id):
    band = Band.objects.get(id=id)

    if request.method == "POST":
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect("band-detail", band.id)
    else:
        form = BandForm(instance=band)

    return render(request, "listings/band_change.html", {"form": form})


def band_delete(request, id):
    band = Band.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == "POST":
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect("band-list")

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request, "listings/band_delete.html", {"band": band})


def listing_change(request, id):
    listing = Listing.objects.get(id=id)

    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect("listing-detail", listing.id)
    else:
        form = ListingForm(instance=listing)

    return render(request, "listings/listing_change.html", {"form": form})


def listing_delete(request, id):
    listing = Listing.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == "POST":
        # supprimer le groupe de la base de données
        listing.delete()
        # rediriger vers la liste des groupes
        return redirect("listing-list")

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request, "listings/listing_delete.html", {"listing": listing})
