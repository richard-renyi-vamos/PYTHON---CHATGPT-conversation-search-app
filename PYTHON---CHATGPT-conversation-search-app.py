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
