import json
import os
from GPSPhoto import gpsphoto
import requests
import shutil
import config
import instaloader

def download_insta_pictures(USERNAME, PASSWORD,PROFILE):
    L = instaloader.Instaloader()
    L.login(USERNAME, PASSWORD)
    for post in instaloader.Profile.from_username(L.context,PROFILE).get_posts():
        L.download_post(post,target= PROFILE)
        
def address(data):
    long = data['Longitude']
    lat = data['Latitude']
    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{long}&key={config.API_KEY}')
    json_response = response.json()
    city = json_response['results'][0]['address_components'][2]['long_name']
    return city



if __name__ == '__main__':
    #Download all instagram pictures
    download_insta_pictures(config.USERNAME, config.PASSWORD,config.PROFILE)

    image_list = os.listdir(os.getcwd() + "/" + config.PROFILE)
    image_list = [a for a in image_list if a.endswith('.jpg')]
    
    for image in image_list:
        print("[*] Found image " + str(image))
        data = gpsphoto.getGPSData(os.getcwd() + f'\\{image}')
        try:
            if data['Latitude']:
                city = address(data)
                print("[*] Found City " + city)
        except:
            print('[*] Image has no Address')
            continue
     
