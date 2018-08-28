import dh_message


dh_message.send_message.send("张飞")
str_info = dh_message.receive_message.receive("张飞")
print(str_info)