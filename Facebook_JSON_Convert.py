import json
import time
import os

# Function to extract messages from JSON and format them
def process_facebook_json(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            # Load the JSON data
            data = json.load(file)

        # Open the output text file
        with open(output_file, 'w', encoding='utf-8') as output:
            # Loop through each message in the JSON data
            for message in data.get('messages', []):
                timestamp = message.get('timestamp_ms', '')
                speaker = message.get('sender_name', '')
                content = message.get('content', '')

                # Convert the timestamp from milliseconds to a readable format
                if timestamp:
                    timestamp = int(timestamp) / 1000  # Convert to seconds
                    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(timestamp))
                else:
                    formatted_time = 'Unknown Timestamp'

                # Create the formatted line
                formatted_message = f"{formatted_time}: {speaker} - {content}\n"
                
                # Write the formatted message to the output file
                output.write(formatted_message)

        print(f"Processed {len(data.get('messages', []))} messages and saved to {output_file}.")

    except Exception as e:
        print(f"An error occurred while processing {input_file}: {e}")

# Process all JSON files in the current folder
def process_all_json_files():
    # Get the current directory
    current_dir = os.getcwd()

    # Loop through all files in the directory
    for filename in os.listdir(current_dir):
        # Check if the file is a JSON file
        if filename.endswith('.json'):
            input_json_file = filename
            output_text_file = filename.replace('.json', '.txt')

            # Process the file and output to the corresponding .txt file
            process_facebook_json(input_json_file, output_text_file)

if __name__ == "__main__":
    process_all_json_files()
