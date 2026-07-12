from groq import Groq
client=Groq(api_key="API-KEY")

def LLmCall(query):
    response= client.chat.completions.create(
       model= "llama-3.1-8b-instant",
       messages= [{"role":"user", "content": query }],
       temperature= 1.0
    )

    print(response.choices[0].message.content)

LLmCall("Make my saturday busy schedule, I am a college student, we have classes from 8:40 to 5")
