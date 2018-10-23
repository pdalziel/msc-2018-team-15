import pprint
import requests



base_url = 'https://api.github.com/repos/'


target_repos = ['Microsoft/vscode', 'tensorflow/tensorflow', 'facebook/react-native', 'torvalds/linux']

client_id = ''
client_secret = ''
access_token = ''

# response_dict = requests.get(base_url+target_repos[0]+'?access_token='+access_token)
# rate_limit_remaining = (response_dict.headers.get('X-RateLimit-Remaining'))
# print(rate_limit_remaining)



# 'X-RateLimit-Limit': '60', 'X-RateLimit-Remaining': '53', 'X-RateLimit-Reset' 'Link': '<https://api.github.com/repositories/41881900/issues?page=2>;
# rel="next", <https://api.github.com/repositories/41881900/issues?page=141>; rel="last"',


def crawl():
    url_str = base_url + target_repos[0] + '/pulls?state=closed'
    #print(url_str)
    #headers = {'Authorization': 'token ' + access_token}
    #response = requests.get(url_str, headers)
    #rate_limit_remaining = (response.headers.get('X-RateLimit-Remaining'))

    #print(response.json())
    #print(rate_limit_remaining)
    #print(response.headers.keys())


    response = requests.get(url_str, headers={"Authorization": access_token})
    print(response.json())
    repos = response.json()
    while 'next' in response.links.keys():
        response = requests.get(response.links['next']['url'], headers={"Authorization": access_token})
        repos.extend(response.json())
        rate_limit_remaining = (response.headers.get('X-RateLimit-Remaining'))
        print(rate_limit_remaining)
        print(response.json())



if __name__ == "__main__":
    crawl()

