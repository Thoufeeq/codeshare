import gmail

g = gmail.login('username@gmail.com', 'password')

g.inbox().mail()

unread_mail = g.inbox().mail(unread=True, sender="thoufeeq.mohd@gmail.com")

if not unread_mail:
        print "Sorry! No new notifications received from the admin."
else:
        unread_mail[0].fetch()
        print "ATTENTION!\n"
        print unread_mail[0].body

# mark as read
for i in unread_mail:
        i.read()

g.logout()
