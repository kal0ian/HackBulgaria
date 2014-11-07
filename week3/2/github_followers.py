import json
import requests
from directedgraph import DirectedGraph


TOKEN = ('bec58496c4930a748bf8468c99ad9cabb1a54a42', '')
r = requests.get(
    'https://api.github.com/users/kal0ian/following', auth=TOKEN)
content = r.json()

class GithubGraph:

    def __init__(self, name):
        self.name = name
        self.edges = {}

    def following(self):
        user_following = []

        for login in content:
            user_following.append(login["login"])
        return user_following
    def is_following(self,username):
        if username in self.following():
            return True
        return False

gitGraph = GithubGraph("GithubGraph")
print (gitGraph.following())
print(gitGraph.is_following("skdls-"))

