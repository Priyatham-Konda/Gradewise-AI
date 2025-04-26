# Gradewise AI

Gradewise AI is a Streamlit project designed for evaluating answer scripts from students scripts photos using the Gemini API and Azure Vision OCR technology. This tool provides an efficient and user-friendly way to assess essay quality directly from uploaded PDF documents.

---

## Features
- Upload PDF files containing answer scripts.
- Automatic evaluation of essays using the Gemini API integration.
- Simple and intuitive interface powered by Streamlit.

---

## Prerequisites
- Python 3.7 or higher
- A valid Gemini API key
- Microsoft Azure Vision API key

---

## Getting Started

Follow the steps below to set up and run Gradewise AI on your local machine.

### Step 1: Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/Priyatham-Konda/Gradewise-AI.git
```

Navigate to the project directory:
```bash
cd Gradewise-AI
```

### Step 2: Create and Activate a Virtual Environment
#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
Install all the required dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### Step 4: Configure Gemini API
Create a configuration file or set environment variables for your Gemini API key to enable essay evaluation.

### Step 5: Run the Application
Start the Streamlit application:
```bash
streamlit run app.py
```

### Step 6: Access the Application
Open your browser and navigate to:
```
http://localhost:8501
```

---

## Contributing
Contributions are welcome! If you'd like to contribute:
1. Fork this repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For queries or feedback, feel free to reach out:
- **Author:** Priyatham Konda
- **GitHub:** [Priyatham-Konda](https://github.com/Priyatham-Konda)
