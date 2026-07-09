import requests
import datetime
import re

def get_latest_cyber_news():
    print("Fetching latest cyber intelligence...")
    # Using an open API to search for top recent cybersecurity stories
    url = "https://hn.algolia.com/api/v1/search?query=cybersecurity&tags=story"
    response = requests.get(url).json()
    
    news_md = "\n"
    # Grab the top 5 stories
    for hit in response['hits'][:5]:
        title = hit['title']
        link = hit['url']
        news_md += f"- 🔴 **[{title}]({link})**\n"
    
    return news_md

def update_readme():
    # Read the current profile README
    with open("README.md", "r") as file:
        readme_content = file.read()

    # Get the fresh news and timestamp
    news_content = get_latest_cyber_news()
    current_time = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    timestamp_md = f"\n*Last updated automatically by GitHub Actions at: {current_time}*\n"

    # Replace the old data between the tags with the new data
    pattern = r"(?<=\n).*?(?=\n)"
    updated_readme = re.sub(
        pattern, 
        news_content + timestamp_md, 
        readme_content, 
        flags=re.DOTALL
    )

    # Save the updated README
    with open("README.md", "w") as file:
        file.write(updated_readme)
    print("Profile successfully updated!")

if __name__ == "__main__":
    update_readme()
