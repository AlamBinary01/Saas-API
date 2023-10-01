import csv
import openai
import json

openai.api_key = 'YOUR_API_KEY'

# Function to get a response from OpenAI GPT-3
def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT-3 engine
        prompt=prompt,
        max_tokens=50  # Adjust as needed
    )
    return response.choices[0].text.strip()

# Function to extract data based on Category or Name
def extract_data(csv_filename, search_key):
    extracted_data = []

    with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            # Split the search_key sentence into words
            words = search_key.split()

            # Check if any word in the sentence matches Category or Name
            if any(word.lower() == row['Category'].lower() or word.lower() == row['Name'].lower() for word in words):
                extracted_data.append(row)

    return extracted_data

# Main loop for the chatbot
while True:
    user_input = input("You: ")  # Get user input

    if user_input == "0":
        break

    # Check if user input starts with "@" (e.g., "@search coffee")
    if user_input.startswith("@search "):
        search_query = user_input[len("@search "):]
        extracted_data = extract_data('futurepedia_tools.xlsx - Sheet1.csv', search_query)

        if extracted_data:
            # Prepare a response with extracted data
            response_data = []
            for entry in extracted_data:
                response_entry = {
                    "Category": entry['Category'],
                    "Name": entry['Name'],
                    "Description": entry['Description'],
                    "URL": entry['URL'],
                    "Photo URL": entry['Photo URL'],
                    "Twitter Link": entry['Twitter Link'],
                    "Facebook Link": entry['Facebook link'],
                    "Instagram Link": entry['Instagram Link'],
                    "Rating": entry['Rating'],
                    "Category 2": entry['Category 2'],
                    "Review 1": entry['Review 1'],
                    "Review 2": entry['Review 2'],
                    "Review 3": entry['Review 3'],
                    "Review 4": entry['Review 4']
                }
                response_data.append(response_entry)
            print(json.dumps(response_data, indent=2))  # Print as JSON
        else:
            print("No data found.")

    else:
        # Use user input as a prompt for the chatbot
        chatbot_prompt = f"You: {user_input}\nAI:"
        chatbot_response = get_openai_response(chatbot_prompt)
        print(chatbot_response)
