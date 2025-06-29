# Asistente de Voz

Un asistente de voz simple desarrollado en Python que permite realizar búsquedas en Amazon mediante comandos de voz.

## Características

- Reconocimiento de voz en español
- Síntesis de voz para responder al usuario
- Búsqueda automática en Amazon

## Requisitos

Para utilizar este asistente de voz, necesitas instalar las siguientes dependencias:

```
pip install SpeechRecognition
pip install gtts
pip install playsound
```

## Cómo usar

1. Ejecuta el script `voicerecognition.py`
2. Cuando el asistente pregunte "¿A qué página vamos hoy día?", responde "Amazon"
3. El asistente te preguntará qué quieres comprar
4. Di el producto que deseas buscar
5. Se abrirá automáticamente el navegador con los resultados de la búsqueda

## Funcionamiento

El programa utiliza:

- `SpeechRecognition` para convertir voz a texto
- `gTTS` (Google Text-to-Speech) para convertir texto a voz
- `playsound` para reproducir los archivos de audio generados
- `webbrowser` para abrir las búsquedas en el navegador

## Personalización

Puedes modificar el código para añadir más sitios web o funcionalidades según tus necesidades.
