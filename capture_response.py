from mitmproxy import http
import json

class ProxyAddon:
    def request(self, flow: http.HTTPFlow) -> None:
        # Modify request here if needed
        pass

    def response(self, flow: http.HTTPFlow) -> None:
        # Capture and dump the response in JSON format
        data = {
            'request': {
                'url': flow.request.url,
                'method': flow.request.method,
                'headers': dict(flow.request.headers),
                'content': flow.request.text,
            },
            'response': {
                'status_code': flow.response.status_code,
                'headers': dict(flow.response.headers),
                'content': flow.response.text,
            }
        }

        with open('network_capture.json', 'a') as f:
            json.dump(data, f, indent=2)
            f.write('\n')

addons = [
    ProxyAddon()
]
