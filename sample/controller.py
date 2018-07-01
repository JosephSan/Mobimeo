from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
from sample.service import Service
import json
import re

hostName = ""
hostPort = 8081


class MyServer(BaseHTTPRequestHandler):
    service = Service()

    def do_GET(self):
        # parse query string
        parsed_url = urlparse(self.path)
        params = dict(qc.split("=") for qc in parsed_url.query.split("&") if len(parsed_url.query) > 0)

        if parsed_url.path == "/lines/":
            try:
                lines = self.service.get_by_time_stop(params["timestamp"], int(params["x"]), int(params["y"]))
                self.wfile.write(bytes(json.dumps([l.name for l in lines]), "utf-8"))
                self.send_response(200)
            except ValueError:
                self.send_response(400)

        elif re.match('/lines/', parsed_url.path):
            line_name = parsed_url.path.split("/")[2]
            is_delayed = self.service.is_line_delayed(line_name)

            if not is_delayed:
                # line does not exist
                self.send_response(400)
            else:
                self.wfile.write(bytes(str(is_delayed), "utf-8"))
                self.send_response(200)

    def do_POST(self):
        print( "incomming http: ", self.path )
        self.send_response(501) # request not supported
