import gmail

g = gmail.login('username@gmail.com', 'password')

g.inbox().mail()

unread_mail = g.inbox().mail(unread=True, sender="thoufeeq.mohd@gmail.com")

for i in unread_mail:
        i.fetch()
        print i.body
        i.read()
        time.sleep(30)

g.logout()
