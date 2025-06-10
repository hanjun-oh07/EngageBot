# User Guide

## Getting Started

### 1. Installation

1. **System Requirements**
   - Python 3.8 or higher
   - Internet connection
   - Web browser

2. **Installation Steps**
   ```bash
   # Clone the repository
   git clone [repository-url]
   cd EngageBot-project

   # Install dependencies
   poetry install

   # Set up environment variables
   cp .env.example .env
   # Edit .env with your OpenAI API key
   ```

### 2. Running the Application

1. **Start the Server**
   ```bash
   poetry run streamlit run main.py
   ```

2. **Access the Application**
   - Open your web browser
   - Navigate to `http://localhost:8501`

## Using EngageBot

### 1. Login

1. **First Time Users**
   - Click "Sign Up"
   - Fill in your profile information
   - Create your account

2. **Returning Users**
   - Enter your credentials
   - Click "Login"

### 2. Chat Scenarios

#### Group Chat Time
1. **Select a Topic**
   - Choose from available discussion topics
   - Topics are age and level appropriate

2. **Start the Conversation**
   - Read the topic introduction
   - Share your thoughts
   - Respond to AI's questions

3. **Continue the Discussion**
   - Build on previous points
   - Ask follow-up questions
   - Express your opinions

#### Breaktime Chat
1. **Enter the Scenario**
   - System selects a random school setting
   - Context is provided automatically

2. **Begin Chatting**
   - Respond naturally to the situation
   - Engage in casual conversation
   - Practice everyday English

3. **Keep the Flow**
   - Follow the conversation naturally
   - Use appropriate language
   - Enjoy the interaction

### 3. Features

#### Profile Management
- Update your information
- Change language level
- Modify preferences

#### Conversation History
- View past conversations
- Track your progress
- Review your interactions

#### Settings
- Adjust notification preferences
- Modify display settings
- Change language preferences

## Best Practices

### 1. For Students

#### Getting the Most Out of Practice
1. **Be Consistent**
   - Practice regularly
   - Set aside dedicated time
   - Track your progress

2. **Engage Actively**
   - Respond thoughtfully
   - Ask questions
   - Express your opinions

3. **Learn from Mistakes**
   - Don't fear errors
   - Note corrections
   - Apply learning

### 2. For Teachers

#### Monitoring Progress
1. **Track Student Activity**
   - Review conversation history
   - Monitor participation
   - Assess improvement

2. **Provide Support**
   - Give feedback
   - Suggest topics
   - Encourage practice

3. **Customize Experience**
   - Adjust difficulty levels
   - Select appropriate topics
   - Modify scenarios

## Troubleshooting

### Common Issues

1. **Login Problems**
   - Check credentials
   - Verify internet connection
   - Clear browser cache

2. **Chat Issues**
   - Refresh the page
   - Check internet connection
   - Try a different browser

3. **Performance Problems**
   - Clear browser cache
   - Check system requirements
   - Update browser

### Getting Help

1. **Documentation**
   - Refer to this guide
   - Check online resources
   - Read FAQs

2. **Support**
   - Contact technical support
   - Submit bug reports
   - Request features

## Advanced Features

### 1. Custom Scenarios

#### Creating New Topics
1. **Topic Structure**
   - Define the context
   - Set difficulty level
   - Specify target age group

2. **Implementation**
   - Follow template format
   - Test thoroughly
   - Get feedback

### 2. Analytics

#### Tracking Progress
1. **Metrics**
   - Conversation length
   - Vocabulary usage
   - Response time

2. **Reports**
   - Generate progress reports
   - Analyze patterns
   - Identify areas for improvement

### 3. Integration

#### External Tools
1. **Learning Management Systems**
   - Connect to LMS
   - Share progress
   - Sync data

2. **Assessment Tools**
   - Link to assessments
   - Track performance
   - Generate reports 