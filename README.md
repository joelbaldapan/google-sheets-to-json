<h1 align="center">
📝 Google Sheets to JSON Converter 📈
</h1>
<p align="center">
<b>Fetch data from a Google Spreadsheet and export it into a local JSON file.</b>
</p>

## 📋 Features
- Uses Google Service Account credentials and Google Sheets API.
- Reads a specific worksheet from a Google Spreadsheet.
- Exports the JSON data to a customizable file path and filename.
- Uses `.env` for configuration.

## 📂 Project Structure

```
google-sheets-to-json/
├── output/                    # JSON files will be exported here (default)
├── .env                       # Environment variables (not committed)
├── .env.example               # Template for the .env file
├── credentials.json           # Service account JSON file credentials
├── main.py                    # Main Python script
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
```

## 🛠️ Setup Instructions

### 1. Clone the Repository

To clone the repository, type this in your terminal:
```bash
git clone https://github.com/joelbaldapan/google-sheets-to-json.git
cd google-sheets-to-json
```

### 2. Install Dependencies

To install the dependencies, type this in your terminal:
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root folder using the provided `.env.example`:

```env
GOOGLE_SHEET_ID=your_google_sheet_id_here
GOOGLE_SHEET_CREDENTIALS=your_credentials_path_here
WORKSHEET_NAME=your_worksheet_name_here

# Optional output settings (Defaults shown below)
OUTPUT_FILE_PATH=output/
OUTPUT_FILE_NAME=output.json

# Optional indent settings (Defaults shown below)
INDENTS=2
```

> 📌 Replace placeholder values with your actual Google Sheet ID, service account credentials path, and worksheet name.

## 🔑 Creating Google Service Account Credentials

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Enable the **Google Sheets API**.
4. Go to **APIs & Services > Credentials**.
5. Click **Create Credentials > Service Account**.
6. After creating, generate a JSON key and save it in your project.
7. Share your Google Sheet with the service account email (e.g., `your-service-account@your-project.iam.gserviceaccount.com`).

## 🚀 Running the Script

```bash
# For Windows
python main.py
```

```bash
# For Mac/Linux
python3 main.py
```

On success, it will generate a JSON file (default: `output/output.json`) from the specified worksheet.

## 📎 Example

Google Sheet URL format:

```
https://docs.google.com/spreadsheets/d/<GOOGLE_SHEET_ID>/...
```

In your `.env`:
```
GOOGLE_SHEET_ID=<GOOGLE_SHEET_ID>
WORKSHEET_NAME=Sheet1
```

## 📦 Output Example

```json
[
    {
        "Name": "Joel Baldapan",
        "Age": 19,
        "Email": "jbemail@example.com"
    },
    {
        "Name": "Angelo Smith",
        "Age": 30,
        "Email": "asemail@example.com"
    }
]
```

## 🧼 Notes

- Empty `OUTPUT_FILE_PATH` or `OUTPUT_FILE_NAME` will default to `output/output.json`.
- Ensure the target worksheet has headers for column names.