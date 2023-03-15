# Given a URL string
# Return the domain name

def domain_name(url):
    # Remove http/https/www
    url = url.replace("http://", "").replace("https://", "").replace("www.", "")
    # Split the remaining from "."
    output = url.split(".")
    return output[0]
