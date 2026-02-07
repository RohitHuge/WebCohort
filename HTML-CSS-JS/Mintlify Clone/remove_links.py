
import re
import os

file_path = r'e:\PROJECTS\Cohort\HTML-CSS-JS\Mintlify Clone\index.html'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Function to replace href in matched <a> tags
    def replace_link(match):
        tag = match.group(0)
        # Check if it has an href
        if 'href=' in tag:
             # Replace double quoted href
            tag = re.sub(r'href="[^"]*"', 'href="javascript:void(0)"', tag)
            # Replace single quoted href
            tag = re.sub(r"href='[^']*'", "href='javascript:void(0)'", tag)
        return tag

    # Regex to match <a> start tags. 
    # Matches <a followed by space, then anything until >
    # Using non-greedy match .*? implies valid HTML structure
    new_content = re.sub(r'(<a\s+[^>]*?>)', replace_link, content, flags=re.IGNORECASE | re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully processed {file_path}")

except Exception as e:
    print(f"Error: {e}")
