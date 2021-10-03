import json
import datetime


with open('message_1.json', 'r') as input_stream, open('messages.txt', 'w+') as output_stream:
    json_data = json.load(input_stream)

    messages = map(lambda x: f'{datetime.datetime.fromtimestamp(x.get("timestamp_ms") / 1000).strftime("%m/%d/%Y %H:%M:%S")} '  # ms to s
                             f'{x.get("sender_name")}: {x.get("content")}\n', 
                             json_data['messages'])

    for line in reversed(list(messages)):
        index = line.find("Reacted ")
        if index == -1:
            output_stream.write(line)