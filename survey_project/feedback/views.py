from django.shortcuts import render, redirect
from .forms import MessageForm

def message_view(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message')
    return render(request, 'message.html', {'form': form})
