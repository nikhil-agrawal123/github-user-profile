import requests

user = str(input('Enter a name of user '))
url = f'https://api.github.com/users/{user}'
url2 = f'https://api.github.com/events'

response1 = requests.get(url2)
with open('events.json', 'w') as f:
    f.write(response1 )

response = requests.get(url)
if response.status_code == 200:
    with open('user.json', 'w') as f:
        f.write(response.text + '\n')
    data = response.json()
    print(f"Username: {data['login']}")
    print(f"Name: {data['name']}")
    print(f"Location: {data['location']}")
    print(f"Bio: {data['bio']}")
    print(f'events_url: {data["received_events_url"]}')