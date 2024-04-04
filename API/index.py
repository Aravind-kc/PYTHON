import os
import requests
def main():
   
    try:
        try:
            api_key = "475f71268bfe4af89fd65418242803"
            data = api_key
            print("first execution",data)
        except Exception as error:
            data = api_key
            print("second execution",data)
        else:
            url = f'https://api.weatherapi.com/v1/current.json?q=coimbatore&key={data}'
            response = requests.get(url=url)
            print(response.text)
    except Exception as e:
        print(e)

main()