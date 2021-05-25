import requests
from csv import writer
channel = 'your_channel_no'
botkey = 'your_bot_key'
sessionid = 'your_session_id'
client_name = 'your_client_name'
def recordConvo(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj: #make sure that the file operation is append ('a+')
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
url = 'https://icap.iconiq.ai/talk' #url of Kuku chatbot server
while True:
        user = input("You: ") #lets you input your chat
        data = {'input': user,
                'botkey': botkey,
                'channel': channel,
                'sessionid': sessionid,
                'client_name': client_name} #data to be passed on POST request
        x = requests.post(url, data = data)
        answer = x.json()
        response_list = answer['responses'] #only filter the 'response' key in json response
        if len(response_list) > 0:
            response = ""
            for i in range(len(response_list)): #sometimes the value of response key is multiple string inside the list this will just combine them all
                response = response + " " + response_list[i]
        else:
            response = answer['responses'][0]
        print(response)
        #print(len(response))
        print("Bot: " + response)
        chat_data = [user, response]
        recordConvo('chat.csv', chat_data)