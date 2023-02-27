from twilio.rest import Client

account_sid = "AC2d94e09d24de6872fcf97f5bb9f90645"

auth_token = "cfbc2db8ef8149a8e9ddea2312731212"

client = Client(account_sid, auth_token)

message = client.messages.create(
	to="+886925282903",
	from_="+12764099428",
	body="你好, 吃晚餐了嗎?")

print(message.sid)