"""Script to wrtie python api and api for pagination"""
import requests
import json

def main():
    try:
        result = {}
        jsn_data = []
        for i in range(10):
            jsn_data.append({"label":i, "value":i})
        result['results'] = jsn_data
        result["has_more"]= "true" if len(result['results']) >= 100 else "false"
        # resp = requests.get("http://localhost:8080/", data=result)
        resp = requests.get("http://localhost:8080/?id=100", data=json.dumps(result),
                            headers={"Content-Type": "application/json"})
        print(resp.data)
    except:
        result = {}
    return result

print(main())
