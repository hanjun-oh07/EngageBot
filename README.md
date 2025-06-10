# EngageBot - English Conversation Practice Platform

EngageBot is an interactive English conversation practice platform designed to help students improve their English speaking skills through natural conversations with AI. The platform provides various chat scenarios that simulate real-life situations students might encounter in their daily lives.

## Features

### 1. User Authentication
- Secure login system
- User profile management
- Session handling

### 2. Chat Scenarios
- **Group Chat Time**: Structured discussions on specific topics
  - Topic selection interface
  - Guided conversation flow
  - Age and language level appropriate responses

- **Breaktime Chat**: Casual conversations in various school settings
  - Random scenario generation
  - Natural conversation flow
  - Context-aware responses

### 3. AI Features
- Personalized responses based on user profile
- Natural conversation flow
- Context-aware follow-up questions
- Supportive and encouraging tone
- Emoji integration for friendly interaction

## Project Structure

```
EngageBot-project/
├── data/                  # Data storage
│   └── user_profiles.json # User profile data
├── langchain_dlab/        # LangChain integration
├── pages/                 # Streamlit pages
│   ├── 3_group_chat.py   # Group chat scenario
│   └── 4_breaktime_chat.py # Breaktime chat scenario
├── tests/                 # Test files
├── main.py               # Main application entry
├── poetry.lock           # Poetry dependency lock
└── pyproject.toml        # Project configuration
```

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd EngageBot-project
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Set up environment variables:
Create a `.env` file with the following:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the application:
```bash
poetry run streamlit run main.py
```

2. Access the application through your web browser at `http://localhost:8501`

3. Log in with your credentials

4. Choose between Group Chat or Breaktime Chat scenarios

## Development

### Adding New Features
1. Create new Streamlit pages in the `pages/` directory
2. Update the sidebar navigation in `main.py`
3. Add necessary LangChain integrations in `langchain_dlab/`

### Testing
Run tests using:
```bash
poetry run pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the GPT models
- Streamlit for the web framework
- LangChain for the AI integration framework
