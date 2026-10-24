tickets=[]
x=0
def ticketinput(x):
    id=x+1
    issue=input("write your complaint ")
    email=input("write your email ")
    return id, issue, email
def add_ticket(a,b,c):
    ticket={
        "id":a,
        "issue":b,
        "mail":c
    }
    tickets.append(ticket)
    return tickets

#taking complaint input


add_ticket(*ticketinput(x))
print(tickets)