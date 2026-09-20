import os
import requests

# Pobieranie tokenu z Secrets na GitHubie
SERVICE_TOKEN = os.environ.get("SERVICE_TOKEN")
API_URL = "https://mtop-beijing.miui.com/gw/mtop.user.blUnlock/apply"

headers = {
    "User-Agent": "Mozilla/5.0 (Android; Mobile)",
    "Cookie": f"new_bbs_serviceToken={SERVICE_TOKEN};",
    "Content-Type": "application/x-www-form-urlencoded"
}

def send_unlock_request():
    print("Wysyłanie wniosku o odblokowanie bootloadera do Xiaomi...")
    try:
        response = requests.post(API_URL, headers=headers, timeout=10)
        print("Odpowiedź z serwera Xiaomi:")
        print(response.text)
    except Exception as e:
        print(f"Błąd podczas wysyłania zapytania: {e}")

if __name__ == "__main__":
    send_unlock_request()
