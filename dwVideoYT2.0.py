import yt_dlp
import os

def descargar_video_o_audio(url, tipo='video', carpeta_descargas='Downloads', mantener_originales=False):
    # Configuración base
    #if not os.path.exists(carpeta_descargas):
    #    os.makedirs(carpeta_descargas)
    
    # Opciones para yt-dlp
    if tipo == 'audio':
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(carpeta_descargas, '%(title)s.%(ext)s'),
        }
    else:  # Video (por defecto)
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'outtmpl': os.path.join(carpeta_descargas, '%(title)s.%(ext)s'),
            'keepvideo': mantener_originales,  # ¡Aquí está la clave!
        }
    
    # Descargar
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("¡Descarga completada en la carpeta:", os.path.abspath(carpeta_descargas))

if __name__ == "__main__":
    url = input("Ingresa la URL de YouTube: ")
    tipo = input("¿Descargar 'video' o 'audio'? (default: video): ").lower() or 'video'
    mantener = input("¿Conservar archivos originales? (s/n, default: no): ").lower() == 's'
    
    descargar_video_o_audio(url, tipo, mantener_originales=mantener)