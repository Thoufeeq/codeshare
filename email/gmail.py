import gmail

g = gmail.login('username@gmail.com', 'password')

g.inbox().mail()

unread = g.inbox().mail(unread=True, sender="thoufeeq.mohd@gmail.com")

unread[0].fetch()
print unread[0].body

# mark as read
for i in unread:
        i.read() 

g.logout()
