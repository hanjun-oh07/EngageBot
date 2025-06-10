# Chat Scenarios

EngageBot provides two distinct chat scenarios to help students practice English conversation in different contexts.

## 1. Group Chat Time

### Overview
Group Chat Time is designed for structured discussions on specific topics. It provides a guided conversation experience where students can practice expressing their opinions and engaging in meaningful discussions.

### Features
- **Topic Selection**: Choose from predefined discussion topics
- **Guided Conversation**: AI facilitates the discussion with appropriate prompts
- **Age-Appropriate Content**: Topics and language level adjusted to user's profile
- **Supportive Environment**: Encouraging and constructive feedback

### Topics
1. Technology and Society
   - Smartphone usage
   - Social media impact
   - Digital learning

2. School Life
   - School uniforms
   - Extracurricular activities
   - Study habits

3. Personal Development
   - Time management
   - Goal setting
   - Stress management

## 2. Breaktime Chat

### Overview
Breaktime Chat simulates casual conversations that might occur during school breaks or free time. It provides a more relaxed environment for practicing everyday English.

### Features
- **Random Scenarios**: Different school settings and situations
- **Natural Conversation Flow**: Casual and spontaneous dialogue
- **Context-Aware Responses**: AI adapts to the conversation context
- **Emotional Intelligence**: Appropriate emotional responses and emojis

### Scenarios
1. **Cafeteria at Lunchtime**
   - Discussing food preferences
   - Sharing weekend plans
   - Talking about classes

2. **School Hallway**
   - Quick catch-ups
   - Making plans
   - Sharing news

3. **On the Way to/from School**
   - Discussing daily routines
   - Talking about weather
   - Sharing experiences

4. **P.E. Class**
   - Sports discussions
   - Team activities
   - Health and fitness

## AI Response Generation

### Context Handling
- Maintains conversation context
- References previous messages
- Adapts to user's language level

### Personalization
- Considers user's age
- Adjusts to language proficiency
- Matches cultural context

### Response Quality
- Natural language flow
- Appropriate vocabulary level
- Culturally sensitive content

## Best Practices

### For Students
1. Be natural and spontaneous
2. Don't worry about mistakes
3. Ask for clarification when needed
4. Practice regularly

### For Teachers
1. Monitor conversation quality
2. Provide feedback when necessary
3. Encourage regular practice
4. Track student progress

## Technical Implementation

### Conversation Flow
```python
# Example conversation flow
1. Initialize chat scenario
2. Load user profile
3. Generate initial context
4. Process user input
5. Generate AI response
6. Update conversation history
```

### Context Management
```python
# Example context handling
context = {
    "user_profile": user_profile,
    "conversation_history": messages[-4:],
    "current_scenario": selected_scenario,
    "language_level": user_profile["language_level"]
}
```

### Response Generation
```python
# Example response generation
response = chain.invoke({
    "question": f"""Previous conversation: {context}
User's response: {user_input}
Please respond naturally and continue the conversation."""
})
``` 