from pprint import pprint
import requests

class stackoverflow:

    def get_questions_with_python_tag(self):
        url = 'https://api.stackexchange.com/2.3/questions?fromdate=1656028800&todate=1656201600&order=desc&sort=activity&tagged=python&site=stackoverflow'
        response = requests.get(url)
        return response.json()

if __name__ == '__main__':
    st = stackoverflow()
    pprint(st.get_questions_with_python_tag())
    a = st.get_questions_with_python_tag()
    for k in a['items']:
        print(k['tags'])
        print(k['link'])