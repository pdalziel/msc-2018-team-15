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
    headers = {'Authorization': 'token ' + access_token}
    response_dict = requests.get(url_str, headers)
    rate_limit_remaining = (response_dict.headers.get('X-RateLimit-Remaining'))

    print(response_dict.json())
    print(rate_limit_remaining)
    print(response_dict.headers.keys())


if __name__ == "__main__":
    crawl()

