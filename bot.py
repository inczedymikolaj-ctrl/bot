import os
import time
import requests
import ntplib

# Pobieranie tokenu z bezpiecznych ustawień GitHuba (Secrets)
SERVICE_TOKEN = os.environ.get("SERVICE_TOKEN")
API_URL = "https://mtop-beijing.miui.com/gw/mtop.user.blUnlock/apply"

headers = {
    "User-Agent": "Mozilla/5.0 (Android; Mobile)",
    "Cookie": f"new_bbs_serviceToken={SERVICE_TOKEN};",
    "Content-Type": "application/x-www-form-urlencoded"
}

def get_exact_beijing_time():
    client = ntplib.NTPClient()
    try:
        response = client.request('pool.ntp.org', version=3)
        return response.tx_time
    except Exception:
        return time.time()

def wait_until_reset():
    print("Bot uruchomiony na GitHub Actions. Oczekiwanie na reset limitu (18:00:00 CEST)...")
    while True:
        current_time = get_exact_beijing_time()
        gmt_struct = time.gmtime(current_time)
        
        # 16:00:00 UTC odpowiada 18:00:00 CEST w Polsce (00:00:00 w Pekinie)
        if gmt_struct.tm_hour == 16 and gmt_struct.tm_min == 0 and gmt_struct.tm_sec == 0:
            print("Godzina 18:00:00! Wysyłanie wniosku...")
            send_unlock_request()
            break
        
        time.sleep(0.05)

def send_unlock_request():
    try:
        response = requests.post(API_URL, headers=headers, timeout=5)
        print("Odpowiedź z serwera Xiaomi:")
        print(response.text)
    except Exception as e:
        print(f"Błąd podczas wysyłania zapytania: {e}")

if __name__ == "__main__":
    wait_until_reset()
