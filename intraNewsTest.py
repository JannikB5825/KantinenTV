import requests
import requests_ntlm

def send_request(url, username, password):
    """
    Sends a request to the url with the credentials specified. Returns the final response
    """
    session = requests.Session()
    session.verify = False
    session.auth = requests_ntlm.HttpNtlmAuth(username, password)
    response = session.get(url)
 
    return response

print(send_request("https://www.bender.de/unternehmen/news","jannik.becker", "BenderCoaster5").text)