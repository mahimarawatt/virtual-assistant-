# Voice-Based Virtual Assistant using Python

## Project Overview

This project is a Python-based voice-controlled virtual assistant developed to automate routine desktop tasks using speech recognition and command-based execution.

The assistant listens to user voice commands and performs actions such as:

- Opening desktop applications
- Sending emails
- Searching the web
- Fetching latest news
- Managing contacts
- Dictionary lookup
- Keyboard-based automation

The system follows a modular architecture where each task is handled by an independent Python module.

---

## Features

- Speech-to-text command detection
- Application launcher automation
- Email sending functionality
- Contact management system
- Real-time news retrieval
- Dictionary word lookup
- Web search support
- Keyboard automation

---

## Project Structure

virtual-assistant/

├── main.py  
├── assistant/  
│   ├── Dictapp.py  
│   ├── GreetMe.py  
│   ├── SearchNow.py  
│   ├── contact.py  
│   ├── detect.py  
│   ├── diction.py  
│   ├── keyboard.py  
│   ├── mail.py  
│   └── news.py  
│  
├── data/  
│   ├── contact_info.json  
│   ├── data.json  
│   └── data.txt  
│  
├── notebooks/  
│   └── dataextract.ipynb  
│  
├── requirements.txt  
└── README.md  

---

## Tech Stack

- Python  
- SpeechRecognition  
- pyttsx3  
- PyAudio  
- PyAutoGUI  
- Requests  
- Wikipedia API  

---

## Installation

Clone the repository:

git clone https://github.com/mahimarawatt/virtual-assistant-

cd virtual-assistant

Install dependencies:

pip install -r requirements.txt

Run the assistant:

python main.py

---

## Example Commands

- Open Chrome  
- Send an Email  
- Search for Python tutorials  
- Show latest news  
- Meaning of Artificial Intelligence  

---

## Use Case

- Task automation  
- Hands-free desktop operations  
- Quick reminders  
- Contact-based communication  
- Productivity support  

---

## Future Enhancements

- NLP-based intent recognition  
- GUI interface  
- Calendar scheduling  
- API integrations  

---

## Author

Mahima Rawat
