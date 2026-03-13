# Stock Analysis Agent

This project is a Python-based stock analysis agent that retrieves stock data and performs analysis using APIs and AI models. The system is designed to automate stock-related insights and assist users in understanding stock performance through programmatic analysis.

The project integrates external APIs and AI-based processing to fetch stock information, process prompts, and generate insights.

---

## Features

* Fetch stock data from external APIs
* AI-powered prompt-based analysis
* Modular Python architecture
* Logging support for debugging
* Token management using tiktoken
* Configurable environment variables
* Utility functions for formatting and processing data

---

## Tech Stack

Programming Language

* Python

Libraries

* requests
* openai
* tiktoken
* google-generative-ai

Other Tools

* Environment variables for API keys
* Logging utilities
* Custom utility modules

---

## Project Structure

```
stock-agent
│
├── main.py
├── stock.py
├── secretary.py
├── util.py
├── requirements.txt
├── log
│   └── custom_logger.py
│
└── README.md
```

---

## Installation

Clone the repository

```
git clone https://github.com/your-username/stock-agent.git
```

Navigate to the project directory

```
cd stock-agent
```

Install dependencies

```
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory and add your API keys.

```
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_api_key
```

---

## Running the Project

Run the main file:

```
python main.py
```

---

## Future Improvements

* Add web interface for stock analysis
* Add visualization of stock trends
* Improve AI analysis pipeline
* Add more financial indicators
* Deploy as a web service

---

## Author

Krishna Ghogare
