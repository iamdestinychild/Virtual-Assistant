import os
import customtkinter
import check_network
import chat_bot



customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.title('Virtual Assistant')
app.geometry("780x520")
app.grid_columnconfigure((0, 1), weight=1)
app.grid_rowconfigure(0, weight=1)
app.resizable(False, False)

appLabel = customtkinter.CTkLabel(app, font=("Arial", 16, 'bold'), text='Virtual Assistant')
appLabel.grid(row=0, column=0, pady=5, sticky="ns")



def networkDialog():
    dialog = customtkinter.CTkToplevel(app)
    dialog.geometry('450x200')
    dialog.title('Network Task')

    label = customtkinter.CTkLabel(dialog, text='Do you want to perform this Task')
    label.pack(pady=20)
    

    def getIp():
        check_network.get_local_ip()
        print(check_network.get_local_ip())
        dialog.withdraw()

    def pingTest():
        check_network.ping_test()
        print(check_network.ping_test())
        dialog.withdraw()

    def portTest():
        result = check_network.network_ports()
        print(result['msg'])
        dialog.withdraw()


    ipTest = customtkinter.CTkButton(dialog, text="Check Ip", command=getIp)
    ipTest.pack(padx=10, side=customtkinter.LEFT)
    ping_test = customtkinter.CTkButton(dialog, text="Ping Test", command=pingTest)
    ping_test.pack(padx=10, side=customtkinter.LEFT)
    Port_test = customtkinter.CTkButton(dialog, text="Check Port", command=portTest)
    Port_test.pack(padx=10, side=customtkinter.LEFT)




# create frames to section Task management and Chat Bot


# task management frame
taskManagement = customtkinter.CTkFrame(app, width=780)
taskManagement.configure(fg_color="transparent")
taskManagement.grid(row=1, column=0, padx=20, sticky="ew")


# for Task we'll do
# > Network Port Test
# > Sort Files
# > Clear Recycle Bin



networkButton = customtkinter.CTkButton(taskManagement, width=220, text="Network Test", command=networkDialog)
networkButton.grid(padx=10, row=0, column=0, sticky='ew')
sortFiles = customtkinter.CTkButton(taskManagement, width=220, text="Sort Files")
sortFiles.grid(padx=10, row=0, column=1, sticky='ew')
clearBin = customtkinter.CTkButton(taskManagement, width=220, text="Clear Bin")
clearBin.grid(padx=10, row=0, column=2, sticky='ew')



# displayBox = customtkinter.CTkTextbox(app, width=680, height=300)
# displayBox.grid(row=2, column=0, columnspan=4, padx=20, pady=20, sticky="ew")


displayBox = customtkinter.CTkScrollableFrame(app, width=680, height=300)
displayBox.grid(row=2, column=0, columnspan=4, padx=20, pady=20, sticky="ew")
    

userFrame = customtkinter.CTkFrame(app, width=780, height=50)
userFrame.configure(fg_color='transparent')
userFrame.grid(row=3, column=0, padx=20, pady=20, sticky='w')

def on_enter(event):
    # print(event)
    messages()


msg_var = customtkinter.StringVar()
userMessage = customtkinter.CTkEntry(userFrame, font=("Arial", 16, "bold"), width=600, height=50, textvariable=msg_var, placeholder_text="Send a message")
userMessage.bind("<Return>", on_enter)
userMessage.grid(row=0, column=0, padx=5)


def messages():

    reply = customtkinter.CTkFrame(displayBox, width=680, height=100)
    # reply.configure(fg_color="transparent")
    reply.pack()

    usermsg = " User: " + userMessage.get()

    bot = chat_bot.bot(userMessage.get())

    bot_reply = " Bot: " + str(bot)

    userMessage.delete(0, customtkinter.END)

    userReply = customtkinter.CTkLabel(reply,  font=("Arial", 16),  anchor="w", width=780, height=50, text=usermsg)
    userReply.pack(pady=5, padx=10)

    MachineReply = customtkinter.CTkLabel(reply,  font=("Arial", 16), anchor="w", justify='left', wraplength=700, width=780, height=50, fg_color='#4b5563', text=bot_reply)
    MachineReply.pack(pady=5, padx=10, expand=False)

   
    # my pc is slow, how do i make it fast?


userButton = customtkinter.CTkButton(userFrame, font=("Arial", 16, "bold"), width=120, height=50, text='Send', command=messages)
userButton.grid(row=0, column=1, padx=5)

app.mainloop()