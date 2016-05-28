import webapp2
import jinja2
import os
import urllib
import json

from webapp2_extras import jinja2
from apiclient.discovery import build
from optparse import OptionParser

class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, **context):
        # Renders a template and writes the result to the response.
        rv = self.jinja2.render_template(_template, **context)
        self.response.write(rv)

class MyHandler(BaseHandler):
    def get(self):
        self.render_response('prueba.html')

#llamado de api youtube
# Set DEVELOPER_KEY to the "API key" value from the Google Developers Console:
# https://console.developers.google.com/project/_/apiui/credential
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyAzz2cH5mm5jzopRC-n9dN-I8_ta3Au8PU"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
class MainHandler(webapp2.RequestHandler):
 
    def post(self):
        PageToken = self.request.get('PageToken')
        SearchText = self.request.get('SearchText')
        youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
        search_response = youtube.search().list(
            q=SearchText,
            part="id,snippet",
            channelId="UCvS6-K6Ydmb4gH-kim3AmjA",
            maxResults=50,
            pageToken=PageToken
        ).execute()

        self.response.write(json.dumps(search_response))
app = webapp2.WSGIApplication([('/test/video', MainHandler),('/test/youtube', MyHandler),], debug=True)
