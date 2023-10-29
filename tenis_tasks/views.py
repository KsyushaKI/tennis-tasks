from django.shortcuts import render
from django.views.generic import FormView
from tenis_tasks.forms import SelectionOfParameters
from pydub import AudioSegment
from gtts import gTTS
import random
import os


class IndexView(FormView):

    form_class = SelectionOfParameters
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        form = SelectionOfParameters(request.POST)
        
        if form.is_valid():

            colors = form.cleaned_data.get('colors')
            colors_count = form.cleaned_data.get('colors_count')
            pause_time = form.cleaned_data.get('pause_time')
            full_time = form.cleaned_data.get('full_time')

            count_repeat_colors = full_time // pause_time
            colors_audio_dir = f"{os.getcwd()}/tenis_tasks/colors_audio/"
            final_dir = f"{os.getcwd()}/tenis_tasks/media/"

            for dir in [colors_audio_dir, final_dir]:
                if not os.path.exists(dir):
                    os.makedirs(dir)
    
            for num in range(count_repeat_colors):
                colors_to_audio = ''
                for _ in range(colors_count):
                    colors_to_audio += ' ' + random.choice(colors)
                audio = gTTS(colors_to_audio, lang='ru', slow=False)
                audio.save(colors_audio_dir + str(num) + "example.mp3")

            sounds = []
            for num in range(count_repeat_colors):
                sounds.append(AudioSegment.from_mp3(colors_audio_dir + str(num) + "example.mp3"))
            combined_sound = sounds[0] + AudioSegment.silent(pause_time * 1000)

            for sound in sounds[1:]:
                combined_sound += sound + AudioSegment.silent(pause_time * 1000)
            combined_sound.export(final_dir + "output.mp3", format="mp3")            

        return render(request, 'index.html') 
