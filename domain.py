from urllib.parse import urlparse

def get_domain_name(url):
    try:
        # get domains(ip adresses) in result variable
        results = get_sub_domain_name(url).split('.')
        # return last two results
        return results[-2] + '.' + results[-1]
    except:
        # in case no links are found
        return ''

def get_sub_domain_name(url):
    try:
        # netloc is network location
        return urlparse(url).netloc
    except:
        return ''
