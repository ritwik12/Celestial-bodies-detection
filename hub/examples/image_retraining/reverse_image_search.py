import requests
import webbrowser
import sys
import base64

def reverseImageSearch(encodedImage):
    searchUrl = 'http://www.google.hr/searchbyimage/upload'
    multipart = {'encoded_image': encodedImage, 'image_content': ''}
    response = requests.post(searchUrl, files=multipart, allow_redirects=False)
    fetchUrl = response.headers['Location']
    return fetchUrl

if __name__ == "__main__":
    filePath = sys.argv[1]
    fetchUrl=reverseImageSearch((filePath, open(filePath, 'rb')))
    webbrowser.open(fetchUrl)