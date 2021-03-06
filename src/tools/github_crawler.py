import pprint
import requests
import json

# https://api.github.com/repos/Microsoft/vscode/pulls?state=closed (131 pages)


base_url = 'https://api.github.com/repos/'


target_repos = ['Microsoft/vscode/pulls', 'tensorflow/tensorflow/pulls', 'facebook/react-native/pulls', 'torvalds/linux/pulls']

client_id = ''
client_secret = ''
access_token = ''

# response_dict = requests.get(base_url+target_repos[0]+'?access_token='+access_token)
# rate_limit_remaining = (response_dict.headers.get('X-RateLimit-Remaining'))
# print(rate_limit_remaining)



# 'X-RateLimit-Limit': '60', 'X-RateLimit-Remaining': '53', 'X-RateLimit-Reset' 'Link': '<https://api.github.com/repositories/41881900/issues?page=2>;
# rel="next", <https://api.github.com/repositories/41881900/issues?page=141>; rel="last"',



def crawl():
    #+ '/pulls?state=closed
    #print(url_str)
    #headers = {'Authorization': 'token ' + access_token}
    #response = requests.get(url_str, headers)
    #rate_limit_remaining = (response.headers.get('X-RateLimit-Remaining'))

    #print(response.json())
    #print(rate_limit_remaining)
    #print(response.headers.keys())
    for slug in target_repos:
        url_str = base_url + slug
        response = requests.get(url_str, headers={"Authorization": access_token})
        print(response.json())
        pulls = response.json()
        while 'next' in response.links.keys():
            response = requests.get(response.links['next']['url'], headers={"Authorization": access_token})
            pulls.extend(response.json())
            rate_limit_remaining = (response.headers.get('X-RateLimit-Remaining'))
            print(rate_limit_remaining)
            print(response.json())
            with open('data.json', 'w') as outfile:
                json.dump(pulls, outfile)



if __name__ == "__main__":
    crawl()

