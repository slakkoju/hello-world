import re
def say_hello():
    return "Hello, World!"

def filterScriptTags(content): 
    oldContent = ""
    while oldContent != content:
        oldContent = content
        content = re.sub(r'<script.*?>.*?</script>', '', content, flags= re.DOTALL | re.IGNORECASE)
    return content

if __name__ == "__main__":
    print(say_hello())
