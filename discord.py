import time
import requests

def main():
    language = input("Sprichst du Deutsch oder Englisch? / Do you speak German or English? ").lower()
    
    if language == 'englisch':
        print("Running the Discord Tool in English.")
    elif language == 'deutsch':
        print("Das Discord-Tool wird auf Deutsch ausgeführt.")
    else:
        print("Invalid language selection. Exiting.")
        return

    webhook_url = input("Bitte gib die Webhook-URL für Discord ein: / Please enter the Discord webhook URL: ")

    print(f"Webhook Name: {get_webhook_name(webhook_url)}")

    action = input("Soll der Webhook einen Link oder eine Nachricht senden? / Should the webhook send a link or a message? ").lower()

    if action == 'link':
        link = input("Bitte gib den Web-Link ein: / Please enter the web link: ")
        send_webhook(webhook_url, content=link)
    elif action == 'nachricht':
        message = input("Bitte verfasse deine Nachricht: / Please compose your message: ")
        send_webhook(webhook_url, content=message)

    author_name = input("Bitte gib den Namen des Autors ein: / Please enter the author's name: ")

    delay = input("Soll die Nachricht sofort, in 5 Minuten oder in 1 Stunde versendet werden? / Should the message be sent immediately, in 5 minutes, or in 1 hour? ").lower()

    if delay == 'sofort':
        send_webhook(webhook_url, username=author_name)
    elif delay == '5 minuten':
        time.sleep(300)
        send_webhook(webhook_url, username=author_name)
    elif delay == '1 stunde':
        time.sleep(3600)
        send_webhook(webhook_url, username=author_name)

def get_webhook_name(webhook_url):
    return webhook_url.split("/")[-1]

def send_webhook(webhook_url, content=None, username=None):
    payload = {'content': content, 'username': username} if content or username else {}
    requests.post(webhook_url, json=payload)
    print("Webhook sent successfully.")
    exit()

if __name__ == "__main__":
    main()# termux-custom-tool
