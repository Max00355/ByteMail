import db

def check(addr):
    messages = []
    b = db.messages.find("messages", {"to":addr})
    if b:
        for x in b:
            if "message" in x:
                message = """
            
            ID: {2}
            From: {0}
            Title: {1}

                """.format(x['from'], x['title'], x['id'])
                messages.append(message)
    return messages
