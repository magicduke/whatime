from twilio.rest import Client

account_sid = "ACf546912b3b42f1a406233c0a9a130965"
auth_token = "f7e2127f2b77b23af7ad7a01e5adac28"

def makeAlarmCall(phone):
    # Your Account Sid and Auth Token from twilio.com/user/account
    client = Client(account_sid, auth_token)
    call = client.calls.create(
        to="+8618668966100",
        from_="+13173533582",
        url="http://demo.twilio.com/docs/voice.xml",
        method="GET",
        status_callback="https://www.myapp.com/events",
        status_callback_method="POST",
        status_callback_event=["initiated", "ringing", "answered", "completed"]
    )
    print(call.sid)