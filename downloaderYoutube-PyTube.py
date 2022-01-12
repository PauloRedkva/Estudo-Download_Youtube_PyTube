import pytube
from pytube import Playlist


# Para Download único - informar o link do vídeo
def downloadURL(url):
    youtube = pytube.YouTube(url)

    # Lista de formato disponiveis
    i = 1
    for lista in youtube.streams.order_by('resolution'):
        try:
            print(lista)
            i += 1
        except:
            pass

    # Conecta para preparar o vídeo
    video = youtube.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').last()

    # Titulo do video
    title = video.title
    print("Iniciando Download : " + str(title))

    # Path do Download (altere aqui)
    video.download("F:/YouTube_Download_PyTube/Download_testes")

    print("Download Concluido!")

# Para Download de Playlist
def downloadPlaylist(url_playlist):
    pl = Playlist(url_playlist)
    i = 1
    print("Iniciando Download Playlist")
    for video in pl.videos:
        video.streams.filter(progressive=True, file_extension="mp4").order_by(
            'resolution').get_highest_resolution().download("F:/YouTube_Download_PyTube/Download_testes") #atento aqui!
        try:
            # Título do video
            title = video.title
            print("Video " + str(i) + ": " + str(title) + " concluído com sucesso!")
            i += 1
        except:
            pass
    print("Iniciando...")
# chamar funcao para download unico
#downloadURL("ENDEREÇO DO VIDEO UNICO")
#download de playlist, copiar url d playlistD") #download de playlist, copiar url d playlist
downloadPlaylist("ENDEREÇO DA PLAYLIST")
# downloadPlaylist
# download de playlist, copiar url de playlist
exit()
