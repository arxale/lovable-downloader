# Lovable API Source Scraper

This Python script fetches the entire source code of a project from the Lovable API and saves it into a local directory.

## Features

* 🚀 Simple configuration via constants in the script
* 📁 Automatically creates directories and subdirectories
* 🔒 Authorization using Bearer Token
* 🐍 Lightweight Python implementation using `requests`

## Table of Contents

* [Requirements](#requirements)
* [Installation](#installation)
* [Configuration](#configuration)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Contributing](#contributing)
* [License](#license)

## Requirements

* Python 3.8 or higher
* Internet access for the API request
* Valid Lovable API token

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/arxale/lovable-downloader.git
   cd lovable-downloader
   ```
2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate     # macOS/Linux
   venv\\Scripts\\activate.bat # Windows
   ```
3. Install the required dependency:

   ```bash
   pip install requests
   ```

## Configuration

Open `a.py` and update the following constants at the top of the file:

```python
# === Configuration ===
API_URL = "https://lovable-api.com/projects/GET-YOUR-PROJECT-ID/source-code"


HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    "Authorization": "Bearer YOUR_API_TOKEN_HERE",
    "Content-Type": "application/json",
    "Origin": "https://lovable.dev",
    "Referer": "https://lovable.dev/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

OUTPUT_DIR = "lovable_source"
```

## Getting Your API Key

You’ll need a valid `Authorization` token from the Lovable API before you can fetch source-code. To grab it:

1. Open your browser’s Developer Tools (e.g. **F12** or **Ctrl+Shift+I**).
2. Switch to the **Network** tab.
3. Trigger any request in the Lovable app (for example by simply reloading the page).
4. Find the call to `GET https://lovable-api.com/.../source-code` in the list.
5. Click that request and open the **Preview** (or **Headers**) sub-panel.
6. Locate the `Authorization` header value (the long `Bearer ...` string) and copy it.
7. Paste it into your `HEADERS["Authorization"]` field in `a.py`).


> **Note:** Make sure you paste your full token without any truncation (`…`).

## Usage

1. Run the script:

   ```bash
   python a.py
   ```
2. A `lovable_source/` directory will be created containing all downloaded files.

## Project Structure

```
├── a.py                # Main scraper script
├── lovable_source/     # Output directory (auto-generated)
└── README.md           # This README file
```

## Contributing

Contributions and improvements are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
