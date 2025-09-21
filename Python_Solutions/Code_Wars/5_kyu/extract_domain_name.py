#Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

#* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
#* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
#* url = "https://www.cnet.com"                -> domain name = cnet"
#"http://google.co.jp"
#"https://123.net"


def domain_name(url):
    if 'www' in url:
        right = url.rsplit('www.',1)[1]
        left = right.rsplit('.',-1)
        return left[0]
    elif '//' in url:
        right = url.rsplit('//',1)[1]
        left = right.rsplit('.',-1)
        return left[0]
    else:
        return url.rsplit('.',-1)[0]


print(domain_name("http://www.zombie-bites.com" ))
print(domain_name("http://google.co.jp"))
print(domain_name("https://123.net"))
print(domain_name("icann.org"))
