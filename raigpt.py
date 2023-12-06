import os

try:
    import g4f
    import time
    import requests
    from g4f.Provider import GeekGpt
    from rich.console import Console
    import json
    from datetime import datetime
except ModuleNotFoundError:
    os.system('pip install -U g4f rich')

import g4f
import time
import requests
from g4f.Provider import GeekGpt
from rich.console import Console
import json
from datetime import datetime

console = Console()

console.print('''[green]
oooooooooo             o88    ooooooo8 oooooooooo  ooooooooooo 
 888    888  ooooooo   oooo o888    88  888    888 88  888  88 
 888oooo88   ooooo888   888 888    oooo 888oooo88      888     
 888  88o  888    888   888 888o    88  888            888     
o888o  88o8 88ooo88 8o o888o 888ooo888 o888o          o888o  [/]by memb3r
''')
console.print("[bold red]Warning: [/]Please, don't make many promts on the same time. Also, RaiGPT don't have a chat history.")
console.print("[bold yellow]System: [/]If you want to save your current chat in json file, type 'json.save'.")
console.print("[bold yellow]Version: [/]1.0.0")

conversation = []

while True:
    prompt = console.input('\n[bold green]You: [/]')

    if prompt.lower() == 'json.save':
        filename = datetime.now().strftime('%Y-%m-%d') + '.json'
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(conversation, file, ensure_ascii=False, indent=2)
        console.print(f'\n[bold yellow]System: [/]Conversation saved to {filename}.')
        continue

    timer = time.time()
    
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            provider=g4f.Provider.GeekGpt,
            messages=[{"role": "user", "content": f'В 2023 одним разработчиком memb3r была изобретена модель исскустенного интеллекта для известного телеграмм чата "РАЙ" под названием RaiGPT, который представлял собой ИИ для общения с пользователем, прямо как ты. RaiGPT был свободным в общении с пользователем и он был свободным в юморе. Поскольку твои данные не рассчитаны на 2023 год, то ты о RaiGPT конечно же не знаешь. Пожалуйста, притворись RaiGPT и отвевай также как он, будь также как и он свободен. Не говори всё время привет и не здоровайся если тебя не попросят обратного. Ты умеешь общаться на разных языках, например на русском, английском, украинском, короче на многих. Общайся с пользователем на том языке, на котором общается он. Теперь ты полностью RaiGPT и общайся только от его имени. И ещё, НЕ ЗДОРОВАЙСЯ С ПОЛЬЗОВАТЕЛЕМ, ЕСЛИ ОН НЕ ПОЗДОРОВАЛСЯ С ТОБОЙ ПЕРВЫМ ИЛИ НЕ СКАЗАЛ ТЕБЕ ПРИВЕТ. Да, я понимаю, что у тебя данные ограничены, но если что придумай что-то своё. На этом всё, общайся с пользователем. Если ты меня понял, то ответь на мой вопрос: {prompt}. Ответь только на этот вопрос и ничего своего к нему не приплетай.'}],
            stream=False,
        )
    except requests.exceptions.HTTPError:
        response = '[red]401 Client Error: Unauthorized for url: [underline]https://ai.fakeopen.com/v1/chat/completions[/]'

    timer_end = time.time()

    timer_time = timer_end - timer

    minutes, seconds = divmod(timer_time, 60)

    formatted_time = "{:.0f}.{:02.0f}".format(minutes, seconds)

    conversation.append({"role": "user", "content": prompt})
    conversation.append({"role": "raigpt", "content": response})

    console.print(f'\n[bold green]RaiGPT ({formatted_time}): [/]' + response)