import os
import asyncio
import customtkinter
from customtkinter import filedialog
import tkinter as tk
import check_network as cn
import chat_bot
import sort_file as sf
import clear_trash as ct
import search as srch



customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.title('Virtual Assistant')
app.geometry("850x520")
app.grid_columnconfigure((0, 1), weight=1)
app.grid_rowconfigure(0, weight=1)
app.resizable(False, False)

appLabel = customtkinter.CTkLabel(app, font=("Arial", 16, 'bold'), text='Welcome To Virtual Assistant 1.5')
appLabel.grid(row=0, column=0, pady=5, sticky="ns")


is_open = False


def networkDialog_task():
    dialog = customtkinter.CTkToplevel(app)
    dialog.geometry('520x220')
    dialog.title('Network Task')
    dialog.resizable(False, False)
    # dialog.attributes('-topmost', True)

    dialog.protocol("WM_DELETE_WINDOW", lambda: close_window(dialog))

    def set_topmost():
        dialog.attributes('-topmost', True)
        app.after(0, dialog.attributes, '-topmost', False)

    dialog.bind("<Map>", lambda event: set_topmost())


    label = customtkinter.CTkLabel(dialog, font=("Arial", 16, 'bold'), text='Which Task Are Your Performing?')
    label.pack(pady=10)
    
    msg_frame = customtkinter.CTkFrame(dialog, fg_color='transparent')
    msg_frame.pack(pady=5)

    msg = ''
    

    msg_label = customtkinter.CTkLabel(msg_frame, font=("Arial", 14), text=msg)
    msg_label.pack(pady=5)

    def getIp():
        cn.get_local_ip()
        msg = f'Your IP is: {cn.get_local_ip()}'
        msg_label.configure(text=msg, text_color='green')

    hosts = ["google.com","twitter.com", "youtube.com"]

    def pingTest():
        
        if(ping_entry.get() == ''):
            msg_label.configure(text='Kindely Choose A Host', text_color='red')
            return
        else:
            host_name = ping_entry.get()
        latency = cn.ping_test(host_name)
        if latency != -1:
            msg = f"{host_name} is reachable with a latency of {latency} ms."
            msg_label.configure(text=msg, text_color='green')    
        else:
            msg = f"ping failed {host_name} is unreachable."
            msg_label.configure(text=msg, text_color='red')




    network_button_frame = customtkinter.CTkFrame(dialog, fg_color='transparent', height=100)
    network_button_frame.pack(pady=5)

    ipTest = customtkinter.CTkButton(network_button_frame, text="Check System Ip", command=getIp)
    ipTest.pack(padx=10, side=customtkinter.LEFT)

    ping_test_frame = customtkinter.CTkFrame(network_button_frame)
    ping_test_frame.pack(padx=10)

    ping_test = customtkinter.CTkButton(ping_test_frame, text="Ping Test", command=pingTest)
    ping_test.pack(padx=1, side=customtkinter.LEFT)

    ping_entry = customtkinter.CTkEntry(ping_test_frame, font=("Arial", 14), placeholder_text="eg google.com")
    ping_entry.pack(padx=5, side=customtkinter.LEFT)

def sortFiles_task():
    dialog = customtkinter.CTkToplevel(app)
    dialog.geometry('520x230')
    dialog.title('Sort File')
    dialog.resizable(False, False)
   
    def set_topmost():
        dialog.attributes('-topmost', True)
        app.after(0, dialog.attributes, '-topmost', False)

    dialog.bind("<Map>", lambda event: set_topmost())

    dialog.protocol("WM_DELETE_WINDOW", lambda: close_window(dialog))

    label = customtkinter.CTkLabel(dialog, font=("Arial", 16, 'bold'), text='Do you have a messy folder, Let\'s SORT it out')
    label.pack(pady=5)

    def choose_folder():
        folder_path = filedialog.askdirectory()
        if folder_path:
            sort_file_path.delete(0, customtkinter.END)
            sort_file_path.insert(0, folder_path)
    

    file_window_frame = customtkinter.CTkFrame(dialog, fg_color='transparent')
    file_window_frame.pack(padx=20, pady=20)


    # direct_var = customtkinter.StringVar()
    sort_file_path = customtkinter.CTkEntry(file_window_frame, font=("Arial", 14), width=350, height=35,placeholder_text="folder path Name")
    sort_file_path.pack(padx=5, side=customtkinter.LEFT)

    file_window_btn = customtkinter.CTkButton(file_window_frame, width=270, height=35, text="Choose Folder", command=choose_folder)
    file_window_btn.pack(padx=5, side=customtkinter.LEFT)

    msg = ''

    sort_msg_frame = customtkinter.CTkFrame(dialog, fg_color='transparent', width=150)
    sort_msg_frame.pack(pady=5)

    sort_msg = customtkinter.CTkLabel(sort_msg_frame, font=("Arial", 14), text='')
    sort_msg.pack()

    def sort_to_folders():
        # global msg
        folder_path = sort_file_path.get()

        if (sort_file_path.get() == ''):
            msg = "Ooops No Folder Selected"
            sort_msg.configure(text=msg, text_color='white')
            return
    
        if not os.path.exists(folder_path):
            msg = f"The {folder_path} folder does not exist. Exiting the program."
            sort_msg.configure(text=msg, text_color='red')
            return
        
        
        msg = sf.sort_files(folder_path)
        sort_msg.configure(text=msg, text_color='white')

    sort_button_frame = customtkinter.CTkFrame(dialog, fg_color='transparent')
    sort_button_frame.pack(pady=5)

    sort_button = customtkinter.CTkButton(sort_button_frame, text="Sort To Folders", width=250, height=35, command=sort_to_folders)
    sort_button.pack()

    
def clearBin_task():
    dialog = customtkinter.CTkToplevel(app)
    dialog.geometry('450x200')
    dialog.title('Clear Bin')
    dialog.resizable(False, False)
    
    def set_topmost():
        dialog.attributes('-topmost', True)
        app.after(0, dialog.attributes, '-topmost', False)

    dialog.bind("<Map>", lambda event: set_topmost())

    dialog.protocol("WM_DELETE_WINDOW", lambda: close_window(dialog))

    label = customtkinter.CTkLabel(dialog, font=("Arial", 16, "bold"), text='Clear Trash Bin')
    label.pack(pady=5)

   
    bin_items_count = ct.bin_count()
    

    bin_count_frame = customtkinter.CTkFrame(dialog, fg_color='transparent', height=40)
    bin_count_frame.pack(pady=5)

    bin_count_label = customtkinter.CTkLabel(bin_count_frame, font=("Arial", 14), text='there are ' + str(bin_items_count) +' items on trash')
    bin_count_label.pack(pady=5)   

    msg_frame = customtkinter.CTkFrame(dialog, fg_color='transparent', height=40)
    msg_frame.pack(pady=5)

    msg = ''
    msg_color = 'white'

    def clear_true():
        global msg

        msg = ct.clear_bin()
        if(str(msg) == 'Bin Is Already Empty'):
             msg_color = 'white'
        if(str(msg) == 'Clear Recircle Bin Succesful'):
             msg_color = 'green'
        if(str(msg) == 'Error Occured'):
             msg_color = 'red'
        
        msg_label.configure(text=str(msg), text_color=msg_color)
        
        bin_items_count = ct.bin_count()
        bin_count_label.configure(text='there are ' + str(bin_items_count) +' items on trash')
        

    
    msg_label = customtkinter.CTkLabel(msg_frame, font=("Arial", 14), text=msg, text_color=msg_color)
    msg_label.pack(pady=5)
    
 
    clear_button_frame = customtkinter.CTkFrame(dialog, fg_color='transparent')
    clear_button_frame.pack(pady=5)


    clear_bin_button = customtkinter.CTkButton(clear_button_frame, width=350, height=45, text="Clear Trash", command=clear_true)
    clear_bin_button.pack(padx=10)
    
  

def find_task():
    dialog = customtkinter.CTkToplevel(app)
    dialog.geometry('750x520')
    dialog.title('Network Task')
    dialog.resizable(False, False)
    
    def set_topmost():
        dialog.attributes('-topmost', True)
        app.after(0, dialog.attributes, '-topmost', False)

    dialog.bind("<Map>", lambda event: set_topmost())

    dialog.protocol("WM_DELETE_WINDOW", lambda: close_window(dialog))

    label = customtkinter.CTkLabel(dialog, font=("Arial", 16, "bold"), text='Lost a file?, No biggie let\'s go on a hunt')
    label.pack(pady=20)

    def choose_folder():
        folder_path = filedialog.askdirectory()
        if folder_path:
            path_entry.delete(0, customtkinter.END)
            path_entry.insert(0, folder_path)
    

    file_window_frame = customtkinter.CTkFrame(dialog, fg_color='transparent')
    file_window_frame.pack(padx=20, pady=20)


    # path_var = customtkinter.StringVar()
    path_entry = customtkinter.CTkEntry(file_window_frame, font=("Arial", 14), width=350, height=35, placeholder_text="default path: C// Or Choose Path")
    path_entry.pack(padx=5, side=customtkinter.LEFT)

    file_window_btn = customtkinter.CTkButton(file_window_frame, width=270, height=35, text="Choose Folder", command=choose_folder)
    file_window_btn.pack(padx=5, side=customtkinter.LEFT)


    # file_name = customtkinter.StringVar()
    file_entry = customtkinter.CTkEntry(dialog, font=("Arial", 14), width=450, height=35, placeholder_text="File/Folder Name")
    file_entry.pack(pady=5)

    async def search():
        msg_label.configure(text='Searching...', text_color='white')
        target_name = file_entry.get()
        if(path_entry.get() == ''):
            file_path ='C://'
        else:
            file_path = path_entry.get()
        found_items = await srch.find_files_and_folders(file_path, target_name)
        for item in found_items:
            paths_found = customtkinter.CTkButton(search_box,  font=("Arial", 16), command = lambda path=item: open_path(path), fg_color='#4b5563', anchor="w", width=780, height=50, text=item)
            paths_found.pack(pady=5, padx=10)
        msg_label.configure(text='Search Complete', text_color='green')

    def async_search():
        asyncio.run(search())

    def open_path(path):
        srch.open_directory(path)

            
            

    search_button = customtkinter.CTkButton(dialog, font=("Arial", 15), width=300, height=45, text='Search', command=async_search)
    search_button.pack(pady=5)

    msg_frame = customtkinter.CTkFrame(dialog, fg_color='transparent')
    msg_frame.pack(pady=5)

    msg_label = customtkinter.CTkLabel(msg_frame, font=("Arial", 16, 'bold'), text='',)
    msg_label.pack()

    search_box = customtkinter.CTkScrollableFrame(dialog, width=1400, height=300)
    search_box.pack(padx=20, pady=20,)

    

   

    


    


    


# create frames to section Task management and Chat Bot


# task management frame
taskManagement = customtkinter.CTkFrame(app, width=1700)
taskManagement.configure(fg_color="transparent")
taskManagement.grid(row=1, column=0, padx=25, sticky="ew")


# for Task we'll do
# > Network Port Test
# > Sort Files
# > Clear Recycle Bin


buttons=[]

def open_window(button):
    for b in buttons:
        if b != button:
            b.configure(state='disabled')
            button.configure(state='disabled')
    if button == networkDialog:
            networkDialog_task()
    elif button == sortFiles:
        sortFiles_task()
    elif button == clearBin:
        clearBin_task()
    elif button == find:
        find_task()

def close_window(win):
    for b in buttons:
        b.configure(state='normal')
    win.withdraw()
    



networkDialog = customtkinter.CTkButton(taskManagement, width=180, height=30, text="Network Test", command=lambda: open_window(networkDialog))
networkDialog.grid(padx=10, row=0, column=0, sticky='ew')
buttons.append(networkDialog)

sortFiles = customtkinter.CTkButton(taskManagement, width=180, height=30, text="Sort Files", command=lambda: open_window(sortFiles))
sortFiles.grid(padx=10, row=0, column=1, sticky='ew')
buttons.append(sortFiles)

clearBin = customtkinter.CTkButton(taskManagement, width=180, height=30, text="Clear Bin", command=lambda: open_window(clearBin))
clearBin.grid(padx=10, row=0, column=2, sticky='ew')
buttons.append(clearBin)

find = customtkinter.CTkButton(taskManagement, width=180, height=30, text="Find", command=lambda: open_window(find))
find.grid(padx=10, row=0, column=3, sticky='ew')
buttons.append(find)




def model_box(msg):

    model_msg = customtkinter.CTkLabel( app, font=("Arial", 16, 'bold'), anchor="w", justify='left', wraplength=7300, width=780, height=50, fg_color='#4b5563',  text=msg)
    model_msg.grid( row=2, pady=20, padx=20)


displayBox = customtkinter.CTkScrollableFrame(app, width=740, height=300)
displayBox.grid(row=3, column=0, columnspan=4, padx=20, pady=20, sticky="s")


userFrame = customtkinter.CTkFrame(app, width=840, height=50)
userFrame.configure(fg_color='transparent')
userFrame.grid(row=4, column=0, padx=20, pady=20, sticky='ew')

def on_enter(event):
    messages()


# msg_var = customtkinter.StringVar()
userMessage = customtkinter.CTkEntry(userFrame, font=("Arial", 16, "bold"), width=650, height=40, placeholder_text="Send a message")
userMessage.bind("<Return>", on_enter)
userMessage.grid(row=0, column=0, padx=5)


def messages():

   

    if userMessage.get() != '':
        reply = customtkinter.CTkFrame(displayBox, width=680, height=100)
        # reply.configure(fg_color="transparent")
        reply.pack()
    
        usermsg = " User: " + userMessage.get()

        bot = chat_bot.bot(userMessage.get())

        bot_reply = " Bot: " + str(bot)

        userMessage.delete(0, customtkinter.END)

        userReply = customtkinter.CTkLabel(reply,  font=("Arial", 16),  anchor="w", wraplength=720, width=780, height=50, text=usermsg)
        userReply.pack(pady=5, padx=10)

        MachineReply = customtkinter.CTkLabel(reply, font=("Arial", 16), anchor="w", justify='left', wraplength=720, width=780, height=50, fg_color='#4b5563', text=bot_reply)
        MachineReply.pack(pady=10, padx=10, expand=False)
    else:
        print('nothing typed')

   
    # my pc is slow, how do i make it fast?


userButton = customtkinter.CTkButton(userFrame, font=("Arial", 16, "bold"), width=120, height=40, text='Send', command=messages)
userButton.grid(row=0, column=1, padx=5)

app.mainloop()