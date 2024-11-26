from configs import Config
import requests
import os
import subprocess


class ThemeEdits:
    def get_api_url(self, id_: int) -> str:
        return f"https://api.opendesktop.org/ocs/v1/content/data/{id_}?format=json"

    def get_link(self, cfg: Config) -> str:
        rsp = requests.get(self.get_api_url(cfg.id_))
        if rsp.status_code == 200:
            js = rsp.json()
            return js["data"][0][f"downloadlink{cfg.index}"]
        else:
            return ""

    def download(self, url: str, cfg: Config):
        if not url:
            print("Dosya bulunamadı.")
            return
        rsp = requests.get(url, stream=True)
        if not os.path.exists(cfg.file_path):
            os.makedirs(cfg.file_path)
        if rsp.status_code == 200:
            with open(cfg.file_path + cfg.file, "wb") as file:
                for chunk in rsp.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"{cfg.file} başarıyla indirildi")
            if cfg.is_compressed:
                self.extract_file(cfg)
                os.remove(cfg.file_path + cfg.file)
        else:
            print("Dosya indirilemedi:", rsp.status_code)

    def extract_file(self, cfg: Config):
        try:
            format_ = cfg.file.split(".")[-1]
            r = ""
            if format_ == "gz":
                r = "z"
            elif format_ == "xz":
                r = "J"

            destination = cfg.file_path
            if cfg.is_folder_need:
                destination = cfg.file_path + cfg.file_name

            if not os.path.exists(destination):
                os.makedirs(destination)

            if format_ == "plasmoid":
                result = subprocess.run(
                    ["unzip", cfg.file_path + cfg.file, "-d", destination],
                    check=True,
                    text=True,
                    capture_output=True,
                )
            elif format_ == "gz" or format_ == "xz":
                result = subprocess.run(
                    ["tar", f"-xv{r}f", cfg.file_path + cfg.file, "-C", destination],
                    check=True,
                    text=True,
                    capture_output=True,
                )
            print(result.stdout)  # Komutun başarılı çıktısını yazdır
            print(f"{cfg.file_path} başarıyla {destination} klasörüne çıkartıldı.")
        except subprocess.CalledProcessError as e:
            print(f"Hata oluştu: {e.stderr}")  # Komutun hata mesajını yazdır
        except FileNotFoundError:
            print(
                "`tar` komutu bulunamadı. Lütfen sisteminizde yüklü olduğundan emin olun."
            )
