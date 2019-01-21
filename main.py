import threading
from queue import Queue
from spider import Spider
from domain import *
from demo import *


PROJECT_NAME ='thesite'
HOMEPAGE = 'https://www.imdb.com'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue= Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)

def crawl():
    # collecting all links on the page
    queued_links= file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links))+' Links in the queue ')
        create_jobs()

def create_jobs():
    # adding links to queue
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
        queue.join()
        # crawling the links
        crawl()

def create_workers():
    # creating multiple spiders by using multithreading
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        # daemon is a background process that is controlled by the user
        t.daemon= True
        t.start()

def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        # telling the spider to terminate
        queue.task_done()
create_workers()
crawl()
