from datetime import datetime
import requests


# CONSTANTS
URL_BASE = 'https://api.github.com/'


# FUNTIONS
def get_github_user(username):
    url = f'{URL_BASE}users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_github_user_followers(username):
    url = f'{URL_BASE}users/{username}/followers'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def download_user_avatar(image_url,name):
    response = requests.get(image_url)
    name1 = name
    if response.status_code == 200:
        response_content = response.content
        # for name in json_followers:
        #     name1 = name['login']
        filename = f'tmp/FollowersPictures/{image_filename()}{name1}.png'
        with open(filename, 'wb') as image:
            image.write(response_content)
            return filename
    return None

def image_filename():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    return timestamp

# def nombre():
#     for each in json_followers:
#         name1 = each['login']
#     return name1

username = input('Give the user name:\t')
user = get_github_user(username)

# if user:
#     user_avatar_url = user.get('avatar_url')
#     download_user_avatar(user_avatar_url)
# else:
#     print('User not found')

# Create a function to download all the follower's pictures given a username.

# print(type(get_github_user(username)))
# print(type(get_github_user_followers(username)))


json_followers = get_github_user_followers(username)
# print(json_followers)
# login = []
# for each in json_followers:
#     value = each['login']
#     login.append(value)

#print(login)
# for each in login:
#     print(each)

if user:
    for each in json_followers:
        download_user_avatar(each['avatar_url'],each['login'])
else:
    print('User not found')