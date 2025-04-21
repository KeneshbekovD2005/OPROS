from django.shortcuts import render, redirect
from .forms import MessageForm

def message_view(request):
    form = MessageForm()
    success = False  # Добавляем переменную success

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            success = True  # Устанавливаем success в True при успешной отправке формы
            return redirect('message')

    return render(request, 'message.html', {'form': form, 'success': success})  # Передаем success в контекст
