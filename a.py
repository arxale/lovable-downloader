import os
import requests

# === Konfiguration ===
API_URL = "https://lovable-api.com/projects/YOURPROJECTID/source-code"
OUTPUT_DIR = "lovable_source"
HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    "Authorization": "Bearer YOUR_TOKEN",
    "Content-Type": "application/json",
    "Origin": "https://lovable.dev",
    "Referer": "https://lovable.dev/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def fetch_source(api_url, headers):
    resp = requests.get(api_url, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    # Debug-Ausgabe – einmalig aktivieren, um Struktur zu sehen
    # print("DEBUG payload type:", type(data), "keys:", data.keys() if isinstance(data, dict) else "")
    # Extrahiere Liste:
    if isinstance(data, dict):
        if "files" in data and isinstance(data["files"], list):
            return data["files"]
        if "data" in data and isinstance(data["data"], list):
            return data["data"]
        # Fall-back, vielleicht ist das dict selbst schon die Liste?
        # (eher unwahrscheinlich)
    if isinstance(data, list):
        return data
    raise RuntimeError("Unbekanntes Antwortformat von der Lovable-API")

def write_files(entries, output_dir):
    written = 0
    for entry in entries:
        # Wir überspringen alles, was kein dict ist
        if not isinstance(entry, dict):
            continue
        name     = entry.get("name")
        content  = entry.get("contents", "")
        binary   = entry.get("binary", False)
        if not name:
            continue

        out_path = os.path.join(output_dir, name)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)

        mode = "wb" if binary else "w"
        with open(out_path, mode) as f:
            if binary:
                # Annahme: Inhalt ist hex-codiert
                f.write(bytes.fromhex(content))
            else:
                f.write(content)
        written += 1

    print(f"✅ Geschrieben: {written} Dateien nach „{output_dir}/“")

def main():
    print("📥 Hole Source-Code von Lovable-API …")
    files = fetch_source(API_URL, HEADERS)
    print(f"🗂 Erstelle Dateien in ./{OUTPUT_DIR}/ …")
    write_files(files, OUTPUT_DIR)

if __name__ == "__main__":
    main()
