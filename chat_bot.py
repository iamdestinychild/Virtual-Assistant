import openai
from dotenv import dotenv_values


openai.api_key = ""

msg_logs = []

def bot(msg):

    while True:

        if msg == '':
           result = 'did not get that!'
        else:
            msg_logs.append({"role":"user", "content":msg})
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=msg_logs
                )

                result = response["choices"][0]["message"]["content"].strip("\n")
                # .strip("\n").strip()

            except Exception:
                result = "Please kindly check your connection"
            
        return result
    





    