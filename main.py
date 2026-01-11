import requests
from bs4 import BeautifulSoup
import rommenu
def gazete_haberleri_getir():
    url = "https://gazete.hacettepe.edu.tr/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    slides = soup.select(".swiper-slide")

    print("Toplam slide:", len(slides))
    print("=" * 50)

    for i, slide in enumerate(slides, 1):
        baslik = slide.select_one(".slide_baslik")
        ozet   = slide.select_one(".slide_ozet")
        link   = slide.select_one(".slide_devam a")

        baslik_text = baslik.get_text(strip=True) if baslik else "Yok"
        ozet_text   = ozet.get_text(strip=True) if ozet else "Yok"
        link_text   = link["href"] if link else "Yok"

        print(f"{i}. Haber")
        print("Başlık:", baslik_text)
        print("Özet  :", ozet_text)
        print("Link  :", link_text)
        print("-" * 50)
def etkinlikler_getir():
    url = "https://etkinlikler.hacettepe.edu.tr/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}

    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    cards = soup.select(".haber_card_ic")

    for i, card in enumerate(cards, 1):
        baslik = card.select_one(".haber_card_baslik")
        detay  = card.select_one(".haber_ozet.mb-2")

        baslik_text = baslik.get_text(strip=True) if baslik else "Yok"
        detay_text  = detay.get_text(strip=True) if detay else "Yok"

        print(f"{i}. Haber")
        print("Başlık:", baslik_text)
        print("Detay :", detay_text)
        print("-" * 40)
def main():
    rommenu.MenuSistemi.karsilama("Hacettepe BBY Bilgi Sistemi")
    
    # Menüde artık sadece duyurular var
    menu_secenekleri = {
        "Duyuruları Listele": gazete_haberleri_getir,
        "Etkinlikleri Listele": etkinlikler_getir,
    }
    
    rommenu.MenuSistemi.menuyuCalistir(menu_secenekleri)

if __name__ == "__main__":
    main()