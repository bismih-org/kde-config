# KDE Desktop Environment Configuration

Bu repository, özelleştirilmiş bir KDE desktop ortamı için hazırlanmış kapsamlı konfigürasyon dosyalarını içerir. Bu ayarlar, kullanıcıya hazır ve optimize edilmiş bir KDE deneyimi sunar.

## 📁 Dosya Yapısı

### Ana Konfigürasyon Dosyaları
- **`.bashrc`** - Bash shell konfigürasyonu ve aliaslar
- **`.zshrc`** - Zsh shell konfigürasyonu (Powerlevel10k teması ile)
- **`.p10k.zsh`** - Powerlevel10k prompt teması ayarları
- **`.gitignore`** - Git için varsayılan ignore kuralları

### KDE Plasma Ayarları
- **`.config/plasma-org.kde.plasma.desktop-appletsrc`** - Plasma desktop widget'ları ve panel ayarları
- **`.config/plasmashellrc`** - Plasma shell ana konfigürasyonu
- **`.config/kdeglobals`** - KDE global ayarları
- **`.config/kwinrc`** - KWin pencere yöneticisi ayarları
- **`.config/konsolerc`** - Konsole terminal ayarları

### Görsel Özelleştirmeler
- **`.gtkrc-2.0`** - GTK2 tema ayarları
- **`.config/gtkrc-2.0`** - GTK konfigürasyonu
- **`.face`** / **`.face.icon`** - Kullanıcı profil resmi (SVG formatında)

### Font ve İkon Ayarları
- **`.fonts.conf`** - Font konfigürasyonu
- **`.fonts/`** - Özel fontlar (D2Coding, MesloLGS NF)
- **`.icons/`** - Özel cursor temaları (Future-cursors, Vimix-white-cursors)

### Plasma Widget'ları
- **`.local/share/plasma/plasmoids/`** - Özel Plasma widget'ları:
  - `org.kde.plasma.eventcalendar` - Etkinlik takvimi (çoklu dil desteği)
  - `com.pajuelo.plasmaConfSaver` - Plasma konfigürasyon kaydetme aracı

### Uygulama Konfigürasyonları
- **`.local/share/kxmlgui5/`** - KDE uygulamaları için UI konfigürasyonları
- **`.local/share/konsole/`** - Konsole profilleri
- **`.local/share/color-schemes/`** - Renk şemaları
- **`.var/app/easyeffects/`** - Easy Effects için hazır ayarlar

## 🚀 Kurulum

### 1. Otomatik Kurulum
```bash
# Repository'yi klonlayın
git clone <repository-url> kde-config
cd kde-config

# Dosyaları home dizinine kopyalayın
cp -r skel/. ~/
```

### 2. Manuel Kurulum
```bash
# Gerekli dizinleri oluşturun
mkdir -p ~/.config ~/.local/share ~/.fonts ~/.icons

# Konfigürasyon dosyalarını kopyalayın
cp skel/.bashrc ~/.bashrc
cp skel/.zshrc ~/.zshrc
cp skel/.p10k.zsh ~/.p10k.zsh
cp -r skel/.config/* ~/.config/
cp -r skel/.local/* ~/.local/
cp -r skel/.fonts/* ~/.fonts/
cp -r skel/.icons/* ~/.icons/
```

## 🎨 Özellikler

### Shell Konfigürasyonu
- **Zsh + Powerlevel10k**: Modern ve hızlı prompt
- **Zinit**: Plugin yöneticisi
- **Fzf-tab**: Gelişmiş tab completion
- **Syntax highlighting**: Komut vurgulama
- **Auto-suggestions**: Otomatik öneriler

### Plasma Desktop
- **Özelleştirilmiş panel**: Sistem monitörleri ve widget'lar
- **Event Calendar**: Google Calendar entegrasyonu
- **Sistem monitörleri**: CPU, RAM, Ağ kullanımı
- **Shortcut'lar**: Optimized klavye kısayolları

### Tema ve Görünüm
- **Breeze tema**: KDE varsayılan tema
- **Fluent-orange-light**: İkon teması
- **Vimix-white-cursors**: Cursor teması
- **Noto Sans font**: Sistem fontu

## 🛠 Gereksinimler

### Temel Paketler
```bash
# KDE Plasma
sudo apt install kde-plasma-desktop

# Shell araçları
sudo apt install zsh git curl

# Font ve tema araçları
sudo apt install fontconfig
```

### Opsiyonel Paketler
```bash
# Zsh eklentileri için
sudo apt install fzf

# Geliştirme araçları
sudo apt install code git-gui

# Multimedia
sudo apt install vlc
```

## ⚙️ Özelleştirme

### Prompt Temasını Değiştirme
```bash
# Powerlevel10k konfigürasyon sihirbazını çalıştırın
p10k configure
```

### Shell Aliasları Düzenleme
Yeni aliaslar eklemek için [`.zshrc`](.zshrc) dosyasını düzenleyin:
```bash
alias yeni-alias='komut'
```

### Plasma Widget'larını Düzenleme
- Panel'e sağ tıklayın → "Panel Options" → "Add Widgets"
- Yeni widget'lar ekleyin veya mevcut olanları yeniden düzenleyin


## 🔧 Sorun Giderme



### Font Sorunları
```bash
# Font cache'ini yenileyin
fc-cache -fv
```

### Plasma Yeniden Başlatma
```bash
# Plasma'yı yeniden başlatın
kquitapp5 plasmashell && kstart5 plasmashell
```

### Widget Sorunları
```bash
# Plasma cache'ini temizleyin
rm -rf ~/.cache/plasma*
```

## 📝 Notlar

- Bu konfigürasyon Debian/Ubuntu tabanlı dağıtımlar için optimize edilmiştir
- İlk açılışta bazı widget'ların yüklenmesi zaman alabilir
- Flatpak uygulamaları için ayrı konfigürasyonlar mevcuttur

## 🤝 Katkıda Bulunma

Bu konfigürasyonu geliştirmek için:
1. Repository'yi fork edin
2. Değişikliklerinizi yapın
3. Pull request gönderin

## 📄 Lisans

Bu konfigürasyon dosyaları MIT lisansı altında dağıtılmaktadır.