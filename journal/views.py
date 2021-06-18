from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import AddJournalForm
from .models import Journal


@login_required(login_url='user:login')
def home_page_view(request):
    context = {}

    journalList = Journal.objects.filter(author=request.user)
    if journalList:
        context.update({"journalList": journalList})

        for journal in journalList:
            if journal.key_moments:
                context.update({"keyMoments": journal.key_moments.split(',')})

    return render(request, 'home.html', context)


@login_required(login_url='user:login')
def add_journal_view(request):
    context = {}

    if request.method == 'POST':
        form = AddJournalForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            titleError = validateTitle(data['title'])
            context.update({"titleError": titleError})
            if not titleError:
                formData = form.save(commit=False)
                formData.author = request.user
                formData.save()
                form = AddJournalForm()
                return redirect("home")

    else:
        form = AddJournalForm()

    context.update({"form": form})

    return render(request, 'add-journal.html', context)


def validateTitle(title):
    titleExists = Journal.objects.filter(title=title).exists()
    if titleExists:
        return "Title already exists!"


def journal_detail_view(request, id):
    data = Journal.objects.get(id=id)

    keyMoments = data.key_moments.split(',')
    context = {
        "data": data,
        "keyMoments": keyMoments,
    }
    return render(request, 'journal_detail.html', context)
