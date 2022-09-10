import string, random, os, sys, _thread, httplib2, time

if len(sys.argv) < 2:
    sys.exit("\033[37mUsage: python3 " + sys.argv[0] + " (Number of threads)")
THREAD_AMOUNT = int(sys.argv[1])
INVALID = [0, 503, 5082, 4939, 4940, 4941, 12003, 5556]

if not os.path.isdir("images_png"):
    try:
        path = "images_png"
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)

def scrape_pictures(thread):
    while True:
        url = 'http://i.imgur.com/'
        length = random.choice((5, 6))
        if length == 6:
            url += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
            url += '.png'

            file_name = url.rsplit('/', 1)[-1]

            h = httplib2.Http('images_png/.cache' + thread)
            response, content = h.request(url)
            if response["status"] == "200" and not b"<!doctype html>" in content:
                out = open(os.path.join('images_png', file_name), 'wb')
                out.write(content)
                out.close()

                file_size = os.path.getsize(os.path.join('images_png', file_name))
                if file_size in INVALID:
                    print("[-] Invalid: " + url)
                    os.remove(os.path.join('images_png', file_name))
                else:
                    print("[+] Valid: " + url)

for thread in range(1, THREAD_AMOUNT + 1):
    thread = str(thread)
    try:
        _thread.start_new_thread(scrape_pictures, (thread,))
    except:
        print('Error starting thread ' + thread)
print('Succesfully started ' + thread + ' threads.')

while True:
    time.sleep(0.01)
