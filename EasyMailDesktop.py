import tkinter as tk # use Tkinter if working in Py 2.x
import smtplib as mail

def writef(a,b):
    
    f_o = open("email_records.txt","a")
    f_o.write(" from "+a+" to "+b+"\n")
    f_o.close()
    
def send_mail():
    '''send_mail(sender,password,reciever,message)->send mail'''
    s=sender.get()
    p=passw.get()
    r=reci.get()
    m=mes.get("1.0",'end-1c')
    writef(s,r)
    import smtplib as mail
    mserver = mail.SMTP("smtp.gmail.com",587)
    mserver.starttls()
    mserver.login(s,p)
    #m=" helllllllo"
    mserver.sendmail(s,r,m)
    mserver.quit()

window = tk.Tk()

l1=tk.Label(window , text="your email")
sender = tk.Entry(window)

l2=tk.Label(window , text="password")
passw = tk.Entry(window)

l3=tk.Label(window , text="recipient")
reci = tk.Entry(window)

l4=tk.Label(window , text="message")
mes = tk.Text(window , height = 10)

sendb = tk.Button(window,text="Send",command=send_mail)

l1.pack()
sender.pack()
l2.pack()
passw.pack()
l3.pack()
reci.pack()
l4.pack()
mes.pack()
sendb.pack()

window.title("send mail")
window.geometry("700x400")
window.mainloop()
