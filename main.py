# app id: 1213788688966877234
# pf19f520b7da44e2ec2c80d30fe147a53c1ef38f4490346355f384c71666d0d8d
import os
import discord
import openai

file = input("Enter 1, 2, or 3 for loading the chat:\n")
match(file):
  case "1":
    file = "chat1.txt"
  case "2":
    file = "chat2.txt"
  case "3":
    file = "chat3.txt"
  case _:
    print("Invalid Choice.")
    exit()

with open (file, "r") as f:
  chat = f.read()

openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.getenv("SECRET_KEY")



#client = OpenAI()


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global chat
        chat += f"{message.author}: {message.content}\n"
        print(f'Message from {message.author}: {message.content}')
        if self.user!=message.author:
          if self.user in message.mentions:
            print(chat)
            response = openai.completions.create(
              model="gpt-3.5-turbo-instruct",
              prompt = f"{chat}\nShahnawazGPT: " ,
              temperature=1,
              max_tokens=256,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0
            )
            channel = message.channel
            messageToSend = response.choices[0].text
            await channel.send(messageToSend)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
