# 🌦️ Agentic AI Weather Assistant

An intelligent, interactive **AI Weather Assistant** built using Streamlit, LangChain, Groq, and the wttr.in weather API. This application uses an AI agent to retrieve current weather information for cities and respond to user questions through a conversational chat interface.

---

## 📌 Project Overview

The Agentic AI Weather Assistant allows users to ask questions about current weather conditions in different cities.

The application uses a LangChain agent powered by a Groq language model. When a user asks about the weather, the agent can call a custom weather tool to retrieve live weather information from wttr.in and provide a clear, natural-language response.

### 🎯 Project Objectives

* Build an AI-powered conversational weather assistant.
* Retrieve current weather information for different cities.
* Understand natural-language weather queries.
* Integrate an AI agent with an external weather API.
* Create an interactive and user-friendly Streamlit interface.

---

## ✨ Features

* 🌡️ **Current Temperature:** Get the current temperature in Celsius.
* 🌤️ **Weather Conditions:** View weather descriptions such as cloudy, sunny, or rainy.
* 🌡️ **Feels-Like Temperature:** Check how warm or cool it feels.
* 💧 **Humidity:** Retrieve the current humidity percentage.
* 💨 **Wind Information:** Get wind speed and direction.
* 👁️ **Visibility:** View visibility information.
* ☀️ **UV Index:** Retrieve the current UV index.
* 🤖 **AI-Powered Chat:** Ask weather questions in natural language.
* 💬 **Chat History:** View previous messages during the session.
* 🔑 **API Key Input:** Enter your Groq API key securely through a password-style sidebar field.
* 🗑️ **Clear Chat:** Clear the current conversation.
* 🎨 **Custom UI:** Responsive layout with custom styling.

---

## 🛠️ Technologies Used

| Technology     | Purpose                             |
| -------------- | ----------------------------------- |
| Python         | Core programming language           |
| Streamlit      | Web application and chat interface  |
| LangChain      | AI agent and tool integration       |
| LangChain Groq | Connects the language model to Groq |
| LangGraph      | Agent execution framework           |
| Groq           | Language model inference            |
| wttr.in        | Weather information API             |
| Requests       | HTTP requests to the weather API    |

---

## 🧠 Project Architecture

```text
              User
               |
               v
      Streamlit Chat Interface
               |
               v
        LangChain AI Agent
               |
               v
          Groq LLM
               |
               v
       Weather Tool Selection
               |
               v
       get_weather(city)
               |
               v
          wttr.in API
               |
               v
       Current Weather Data
               |
               v
        AI Response
               |
               v
       Streamlit Chat UI
```

---

## 📂 Project Structure

```text
Agentic-AI-Weather-Assistant/
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
└── .streamlit/
    └── secrets.toml  # Optional
```

**Note:** The `.streamlit/secrets.toml` file is optional because the application also supports entering the API key through the sidebar.

---

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Agentic-AI-Weather-Assistant.git
```

Navigate to the project folder:

```bash
cd Agentic-AI-Weather-Assistant
```

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

### Step 3: Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Step 4: Configure the Groq API Key

1. Create or sign in to your Groq account.
2. Generate an API key from the Groq Console.
3. Launch the application.
4. Enter your API key in the sidebar.

Keep your API key private. Never commit it to GitHub.

### Step 5: Run the Application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

---

## 📦 Requirements

Create a `requirements.txt` file with:

```text
streamlit
langchain
langchain-groq
langgraph
requests
```

---

## 💬 Example Questions

Try these questions in the chatbot:

```text
What is the weather in Bengaluru?

Tell me the current weather in Mumbai.

What is the temperature in Delhi?

How humid is it in London?

Tell me the wind speed in Chennai.

Compare the weather in London and Paris.
```

---

## 🔍 How It Works

1. The user enters a weather-related question in the Streamlit chat interface.
2. The LangChain agent receives the question.
3. The Groq language model determines whether to use the weather tool.
4. The `get_weather()` tool sends a request to wttr.in.
5. The API returns weather information in JSON format.
6. The agent uses the returned information to prepare a natural-language response.
7. Streamlit displays the response and saves it in the current session's chat history.

---

## 🔐 API Key Security

The application accepts a Groq API key through the Streamlit sidebar. An optional `secrets.toml` file can also be used for local configuration.

Example:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Store this file inside the `.streamlit` folder.

**Security recommendations:**

* Never hardcode API keys in your source code.
* Never upload API keys or `secrets.toml` to GitHub.
* Add secrets files to `.gitignore`.
* Revoke and replace any API key that has been exposed.

---

## ⚠️ Limitations

* Weather information depends on the availability and accuracy of the wttr.in service.
* Internet access is required.
* Groq API access and usage limits may apply.
* The application retrieves current weather conditions; it is not designed as a dedicated long-range forecasting system.
* Chat history is maintained in the Streamlit session and is not stored in a permanent database.
* Weather data may be unavailable for some locations.

---

## 🚀 Future Improvements

* Add a multi-day weather forecast.
* Display weather information using charts and weather icons.
* Add location search suggestions.
* Include air quality and rainfall information.
* Add a map-based weather interface.
* Store chat history in a database.
* Deploy the application online.
* Add voice-based weather queries.

---

## 🎓 Learning Outcomes

Through this project, you can learn:

* How to create a Streamlit application.
* How to build an AI agent using LangChain.
* How to integrate Groq language models.
* How to define and use custom tools.
* How to connect an application to an external API.
* How to manage chat history using Streamlit session state.
* How to handle API errors and configure environment secrets.

---

## 👨‍💻 Author

**Yanaguntikar Meesal**

GitHub: [Your GitHub Profile](https://github.com/YOUR_USERNAME)

---

## 📄 License

This project is intended for educational and learning purposes. You may add an MIT License or another suitable license to your repository.

---

⭐ If you find this project useful, consider giving the repository a star on GitHub.
