CHATGPT CONVERSATION

************

create a PYTHON code with CHATGPT API to seach between my AI conversations
ChatGPT said:
Here’s a Python script that allows you to search through your ChatGPT conversation history using the OpenAI API. It assumes you have saved your past conversations as text or JSON files. The script will process those files and search for relevant keywords.

Search Chatgpt Api

Answer in chat instead
This script looks through stored ChatGPT conversation files in JSON format, searching for messages that contain your query. You can save past conversations and use this tool to quickly find relevant discussions. 🚀 Let me know if you need modifications! 😊

***********

import openai
import json
import os

def search_conversations(api_key, query, history_folder="chat_history"):
    """
    Searches for a keyword or phrase in saved conversation history.
    """
    results = []
    
    # Ensure history folder exists
    if not os.path.exists(history_folder):
        print("No conversation history found.")
        return []
    
    # Iterate through conversation files
    for filename in os.listdir(history_folder):
        if filename.endswith(".json"):  # Assuming JSON format
            with open(os.path.join(history_folder, filename), "r", encoding="utf-8") as file:
                data = json.load(file)
                for message in data.get("messages", []):
                    if query.lower() in message.get("content", "").lower():
                        results.append({
                            "file": filename,
                            "role": message.get("role"),
                            "content": message.get("content")
                        })
    
    return results

if __name__ == "__main__":
    OPENAI_API_KEY = "your-api-key-here"  # Replace with your actual API key
    search_query = input("Enter search term: ")
    
    search_results = search_conversations(OPENAI_API_KEY, search_query)
    
    if search_results:
        print("\nSearch Results:")
        for result in search_results:
            print(f"File: {result['file']} | Role: {result['role']}\nMessage: {result['content']}\n---")
    else:
        print("No matches found.")
