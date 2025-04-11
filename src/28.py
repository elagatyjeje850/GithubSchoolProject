# This is an example of how to write code on GitHub
import requests

def main():
    # Replace this with your own data source
    url = "https://raw.githubusercontent.com/example/user-data/master/data.json"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        user_data = response.json()
        
        # Process the data and save it to a file
        with open("data.txt", "w") as f:
            for item in user_data:
                f.write(f"{item['name']}, {item['age']} years old\n")
    
    else:
        print("Error: ", response.status_code)

if __name__ == "__main__":
    main()
