def print_github_issues():
    import requests
    from bs4 import BeautifulSoup

    url = "https://github.com/schoolproject"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    issues_list = soup.find_all('li', class_='list-group-item')
    
    for issue in issues_list:
        title = issue.find('h2').text
        description = issue.find('div', class_='detail-description').text
        print(f"Title: {title}")
        print(f"Description:\n{description}\n")
