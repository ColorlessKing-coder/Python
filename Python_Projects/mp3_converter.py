import os
import yt_dlp
from pydub import AudioSegment
import requests
import time


class PolisAnimasyonu:
    def __init__(self):
        self.blue = "\033[94m"
        self.red = "\033[91m"
        self.reset = "\033[0m"

        self.frames = [
            "▓▒░░░░░░░░░░░░░░░░░░░░",
            "▓▓▒░░░░░░░░░░░░░░░░░░░",
            "▓▓▓▒░░░░░░░░░░░░░░░░░░",
            "▓▓▓▓▒░░░░░░░░░░░░░░░░░",
            "▓▓▓▓▓▒░░░░░░░░░░░░░░░░",
            "▓▓▓▓▓▓▒░░░░░░░░░░░░░░░",
            "▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░",
            "▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░",
            "▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░",
            "▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░",
            "▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░",
            "▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░",
            "▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░",
            "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░",
            "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░",
            "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░",
            "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░",
            "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░",
            "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░",
            "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░",
            "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒",
        ]

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def play_animation(self):
        for frame in self.frames:
            self.clear_console()
            print(" " * 10 + self.red + frame + self.reset + " " * 10 + self.blue + frame + self.reset)
            self.print_ascii_cars(self.red, self.blue)
            time.sleep(0.1)

        for frame in self.frames:
            self.clear_console()
            print(" " * 10 + self.blue + frame + self.reset + " " * 10 + self.red + frame + self.reset)
            self.print_ascii_cars(self.blue, self.red)
            time.sleep(0.1)

    def print_ascii_cars(self, left_color, right_color):
        print("\n" + " " * 6 + left_color + "    ____          ____    " + self.reset + "     " + right_color + "    ____          ____    " + self.reset)
        print(" " * 6 + left_color + "  _/__|__\\____  _/__|__\\____ " + self.reset + "     " + right_color + "  _/__|__\\____  _/__|__\\____ " + self.reset)
        print(" " * 6 + left_color + " |  _     _   ||  _     _   |" + self.reset + "     " + right_color + " |  _     _   ||  _     _   |" + self.reset)
        print(" " * 6 + left_color + " '-(_)-------(_)-' -(_)-------(_)-" + self.reset + "     " + right_color + " '-(_)-------(_)-' -(_)-------(_)-" + self.reset)


class VideoIslemleri:
    def __init__(self):
        self.ffmpeg_yolu = r'C:\Users\WhereIsHome\AppData\Local\Microsoft\WinGet\Links'

    def url_kontrol(self, url):
        try:
            req = requests.get(url)
            if req.status_code == 200:
                print("Bağlantı geçerli.")
                return url
            else:
                print("Bağlantı adresini kontrol edin.")
                return None
        except Exception as e:
            print("Hata: ", e)
            return None

    def video_indir_url(self, url, file_name):
        hedef_dizin = os.path.join(f'C:\\Users\\{os.getlogin()}\\Desktop', file_name or 'Sarkilar')
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(hedef_dizin, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': self.ffmpeg_yolu
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            mp3_file = ydl.prepare_filename(info_dict).replace('.webm', '.mp3').replace('.m4a', '.mp3')
            return mp3_file

    
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    def check_and_convert_to_mp3(self, input_file):
        file_extension = os.path.splitext(input_file)[1].lower()
        if file_extension == '.mp4':
            mp3_filename = os.path.splitext(input_file)[0] + ".mp3"
            audio = AudioSegment.from_file(input_file)
            audio.export(mp3_filename, format="mp3")
            print(f"MP3'e dönüştürüldü: {mp3_filename}")
            return mp3_filename
        print("Bu dosya MP4 formatında değil.")
        return input_file


class DosyaIslemleri:
    def __init__(self, file_name="Sarkilar"):
        self.file_name = file_name
        self.file_path = os.path.join(f'C:\\Users\\{os.getlogin()}\\Desktop', self.file_name)

    def make_file(self):
        if not os.path.exists(self.file_path):
            os.makedirs(self.file_path, exist_ok=True)

    def file_exists(self):
        return os.path.exists(self.file_path)


def main():
    animasyon = PolisAnimasyonu()
    animasyon.play_animation()

    video_islem = VideoIslemleri()
    dosya = DosyaIslemleri()

    print("")
    print("")
    print("Not : Eğer Oynatma Listesi Bağlantısını Seçerseniz Tüm Oynatma Listesini İndirecektir Fakat Sadece Şarkı Urlsini Sçerseniz Sadece Şarkıyı İndirecektir ")
    
    dosya_adi = input("Dosya İsmi Ne Olsun : ")
    url = input("Url Adresini Giriniz Yada Çıkış İçin q Harfine Basınız: ")
    if url.lower() != "q":
        if video_islem.url_kontrol(url):
            dosya.make_file()
            mp3_file = video_islem.video_indir_url(url, dosya_adi)
            video_islem.check_and_convert_to_mp3(mp3_file)

    
if __name__ == '__main__':
    main()
