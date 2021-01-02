import requests

# SETTINGS

endpoint_url = "https://api.spotify.com/v1/me/tracks"
token = "BQDab9waJPvKQHd9-vMK14aRqSSmGkwwKrDxOjjfrJo_spcBvSzGyzz6xuwquwf9b1KGSNGZ5LANEKbA_zvTz8W2k3jrCdipfAMSH7ENw8z7mPA6Vq3AFtS-0MPXp3qnQN8cGsZLMrtM1W9WHLqHASWf_Cxxp57BnJb4tuuFOHOJhf6u7Lj3vMqzT1LBuBh9KY-ywn40uuScKtWFq3zGcRt3LkQhZwwVSHzAMEGD0737Wsd15Lwh_QA2TvPA3DjgUV1Kstfpo1i4vDkAe7WQZfckKFiW3cgftJI"
user_id = "c9be82ms3mnt1ebamsarvgj1y"

uris = []

response = requests.get(endpoint_url,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {token}"})

json_response = response.json()
if list(json_response.keys()) == ['error']:
    print(json_response['error'])
#print("Rec keys:",json_response.keys())
#print(json_response['items'])
#print('Saved Songs:')
for i,j in enumerate(json_response['items']):
            track = j['track']
            #print("track:", track.keys())
            uris.append(track['uri'])
            #print(f"{i+1}) \"{track['name']}\" by {track['artists'][0]['name']}")

# CREATE A NEW PLAYLIST

import requests
import json

endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

request_body = json.dumps({
          "name": "Today's saved songs",
          "description": "My first programmatic playlist, yooo!",
          "public": False
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json",

                                                                           #"Accept":"application/json",
                        "Authorization": f'Bearer {token}'  #,"Encoding":wer5"Content-Transfer-Encoding"
                                                                           })

json_response = response.json()
if list(json_response.keys()) == ['error']:
    print(json_response['error'])
url = json_response['external_urls']['spotify']
print(response.status_code)

# FILL THE NEW PLAYLIST

playlist_id = response.json()['id']
print("playlist_id", playlist_id)

endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

request_body = json.dumps({
          "uris" : uris
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {token}"})

print(response.status_code)
json_response = response.json()
if list(json_response.keys()) == ['error']:
    print(json_response['error'])

print(f'Your playlist is ready at {url}')
