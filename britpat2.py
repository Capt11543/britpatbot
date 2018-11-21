import asyncio
import discord
import random as ra
import datetime

client = discord.Client()

token = "NDkwNjkxMTEwOTAyMDM4NTM4.Dn9AIg.Yto767aawLn7IrI-wRXpdi1AeBI"
brits = [ "338795697081942018", "381657087031246858", "490691110902038538" ]
responses = [ "England is my city!",
              "Oi m8!  You got a loiscense for that?",
              "https://cdn.discordapp.com/attachments/461999646546329685/468954292309590028/yeets.PNG",
              "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Theresa_May.png/220px-Theresa_May.png",
              "https://cdn.vox-cdn.com/thumbor/D6_O907jNEs8krJdVL6JfoTDNAk=/0x0:590x760/1200x800/filters:focal(246x184:340x278)/cdn.vox-cdn.com/uploads/chorus_image/image/53246041/Sir_Winston_Churchill___19086236948.0.jpg",
              "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Queen_Elizabeth_II_in_March_2015.jpg/220px-Queen_Elizabeth_II_in_March_2015.jpg",
              "Never, never, never give up.",
              "You have enemies? Good. That means you've stood up for something, sometime in your life.",
              "The best argument against democracy is a five-minute conversation with the average voter.",
              "https://cdn.discordapp.com/attachments/488046014478155776/490681275481587713/M9SpXml.png",
              "https://cdn.discordapp.com/attachments/488046014478155776/490683078197379083/Z.png",
              "There is a forgotten, nay almost forbidden word, which means more to me than any other. That word is England.",
              "Rule, Brittania!  Brittania rule the waves!",
              ":flag_gb: :flag_gb: :flag_gb: :flag_gb:",
              "Be England what she will, with all her faults she is my country still.",
              "Remember that you are an Englishman, and have consequently won first prize in the lottery of life.",
              "ENGLAND, with all thy faults, I love thee still,	My country! and, while yet a nook is left Where English minds and manners may be found,	Shall be constrained to love thee.",
              "https://www.youtube.com/watch?v=tN9EC3Gy6Nk" ]
cbh_responses = [ ":cloud_lightning: The Clickbait Hour :cloud_lightning:",
                  "https://cdn.discordapp.com/attachments/339580111999205376/491011824297443338/Screenshot_1.PNG",
                  "https://cdn.discordapp.com/attachments/339580111999205376/491012061577347112/asfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png"]

@client.event
async def on_ready():
    print(":3")

@client.event
async def on_message(message):
    # Replies to a British person
    for x in brits:
        if message.author.id == x:
            if ra.randint(1, 11) == 10:
                await client.send_message(message.channel, responses[ra.randint(0,len(responses) - 1)])
                print("Chance successful")
            else:
                print("Chance failed")

    # Responds to mention
    if client.user in message.mentions and message.author != client.user:
        await client.send_message(message.channel, responses[ra.randint(0, len(responses) - 1)])
        print("Responded to mention")

    #Responds to PM
    if message.channel.is_private and message.author != client.user:
        await client.send_message(message.channel, responses[ra.randint(0, len(responses) - 1)])
        print ("Responded to PM")

    if "britpatbot" in message.content.lower():
        await client.send_message(message.channel, ":3")
        print("I was caled by my nickname!")

    # Reacts to a message depending on which country it is
    if "britain" in message.content.lower() or "england" in message.content.lower() or "the uk" in message.content.lower() or "the u.k." in message.content.lower() or "british" in message.content.lower() or "english" in message.content.lower():
        await client.add_reaction(message, '👍')
        print("Thumbs-up!")
    if "america" in message.content.lower() or "the united states" in message.content.lower() or "the us" in message.content.lower() or "usa" in message.content.lower() or "the u.s." in message.content.lower() or "u.s.a." in message.content.lower():
        await client.add_reaction(message, '👎')
        print("Thumbs-down.")

client.run(token)