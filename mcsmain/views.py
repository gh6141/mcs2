from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


from mcsmain.models import Mcsmain,Comment
from mcsmain.forms import McsmainForm,CommentForm


def top(request):
    mcsmain = Mcsmain.objects.all()
    context = {"mcsmain": mcsmain}
    return render(request, "mcsmain/top.html",context)



# Create your views here.

@login_required
def mcsmain_new(request):
    if request.method == 'POST':
        form = McsmainForm(request.POST)
        if form.is_valid():
            mcsmain = form.save(commit=False)
            mcsmain.created_by = request.user
            mcsmain.save()
            return redirect(mcsmain_detail, mcsmain_id=mcsmain.pk)
    else:
        form = McsmainForm()
    return render(request, "mcsmain/mcsmain_new.html", {'form': form})


@login_required
def mcsmain_edit(request, mcsmain_id):
    mcsmain = get_object_or_404(Mcsmain, pk=mcsmain_id)
    if mcsmain.created_by_id != request.user.id:
        return HttpResponseForbidden("このメッセージの編集は許可されていません。")

    if request.method == "POST":
        form = McsmainForm(request.POST, instance=mcsmain)
        if form.is_valid():
            form.save()
            return redirect('mcsmain_detail', mcsmain_id=mcsmain_id)
    else:
        form = McsmainForm(instance=mcsmain)
    return render(request, 'mcsmain/mcsmain_edit.html', {'form': form})


@login_required
def mcsmain_detail(request, mcsmain_id):
    mcsmain = get_object_or_404(Mcsmain, pk=mcsmain_id)
    comments=Comment.objects.filter(commented_to=mcsmain_id).all()
    comment_form=CommentForm()
    return render(request, 'mcsmain/mcsmain_detail.html',
                  {'mcsmain': mcsmain,'comments':comments,'comment_form':comment_form,})

@login_required
def comment_new(request,mcsmain_id):
    mcsmain = get_object_or_404(Mcsmain, pk=mcsmain_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commented_to=mcsmain
            comment.commented_by = request.user
            comment.save()
            messages.add_message(request,messages.SUCCESS,"コメントを投稿しました。")
    else:
        messages.add_message(request,messages.ERROR,"コメントの投稿に失敗しました。")
    return redirect('mcsmain_detail',mcsmain_id=mcsmain_id)


