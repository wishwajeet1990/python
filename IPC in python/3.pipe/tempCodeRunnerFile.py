while True :
    reply = input("Enter input :")
    if reply.lower() == "quit":
        print("Chat ended")
        break
    else:
        print("You entered :- " ,reply)