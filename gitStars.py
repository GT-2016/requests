# coding:utf-8

"""
github for popular stars project by python
"""
import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status Code",r.status_code)

# api response save to an params
reponse_dict = r.json()
print(reponse_dict.keys())



# 是否受速率限制
# rate_url = "https://api.github.com/rate_limit"
"""
{
  "resources": {
    "core": {
      "limit": 60,
      "remaining": 59,
      "reset": 1530101872
    },
    "search": {
      "limit": 10,
      "remaining": 10,
      "reset": 1530099025
    },
    "graphql": {
      "limit": 0,
      "remaining": 0,
      "reset": 1530102565
    }
  },
  "rate": {
    "limit": 60,
    "remaining": 59,
    "reset": 1530101872
  }
}
"""
