import subprocess
import json

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    command = ["curl", url]
    
    try:
        # Run the curl command and capture its output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        # Parse the JSON response
        data = json.loads(result.stdout)
        children = data.get("data", {}).get("children", [])
        # Print the titles of the posts
        for child in children:
            title = child.get("data", {}).get("title", "")
            print(title)
    except subprocess.CalledProcessError as e:
        # If the curl command fails (returns a non-zero exit status), print the error message
        print(f"Error executing curl command: {e}")
    except json.JSONDecodeError as e:
        # If the JSON parsing fails, print the error message
        print(f"Error parsing JSON: {e}")

if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    top_ten(subreddit)