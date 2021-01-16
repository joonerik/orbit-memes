import slack
import os
import json
import ast
import requests
from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# app = App(
#     token=os.environ.get("BOT_SLACK_TOKEN"),
#     signing_secret=os.environ.get("APP_SIGNING_SECRET")
# )

client = slack.WebClient(token = os.environ['BOT_SLACK_TOKEN'])
user_client = slack.WebClient(token = os.environ['USER_SLACK_TOKEN'])
app_client = slack.WebClient(token = os.environ['APP_SLACK_TOKEN'])
channels = client.conversations_list()
general_channel = 'C0BCSRVAQ'
# retrieve list of already downloaded memes
file = open('memes_id.txt', 'r')
saved_files_id = []
for id in file:
    saved_files_id.append(id[:-1])
file.close()

def fetch():
    str_files = str(client.files_list(channel=general_channel))
    dict_files = ast.literal_eval(str_files)

    file_txt = open('memes_id.txt', 'a')
    for file in dict_files["files"]:
        if file["id"] not in saved_files_id:
            # somehow the shared property switches on and off.
            # user_client.files_revokePublicURL(file=file["id"])
            user_client.files_sharedPublicURL(file=file["id"])

            str_public_file = str(user_client.files_info(file=file["id"]))
            public_file = ast.literal_eval(str_public_file)
            
            wrong_file_url = public_file["file"]["permalink_public"]
            title = public_file["file"]["title"]

            file_url = correct_url(wrong_file_url, title)

            file_txt.write(file["id"] + '\n')
            print("Wrote ID to file: " + file["id"])
            print("File_url: " + file_url)
            save(file_url, title)

    file_txt.close()

def correct_url(file_url, title):
    f = file_url
    f = f[24:].split('-')
    prefix = "https://files.slack.com/files-pri/"
    file_url = (prefix + f[0] + "-" + f[1] + "/" 
                + title + "?pub_secret=" + f[2])
    return file_url

def save(file_url, title):
    photo_req = requests.get(file_url)
    if photo_req.status_code == 200:
        # the split might be dangerous in case of titles containing a dot
        open('memes/' + title.split('.')[0] + '.jpg', 'wb').write(photo_req.content)
        print("saved")

def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    # client.chat_postMessage(channel='#general', text=text)
    files = client.files_list(channel='general')

fetch()