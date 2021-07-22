
from win10toast import ToastNotifier

def notification(title, desc):
    notify = ToastNotifier()
    notify.show_toast(
        title, 
        desc,
        icon_path=None,
        duration=10
    )
# notification("Email Sent!","You email has been sent. Successfully!")