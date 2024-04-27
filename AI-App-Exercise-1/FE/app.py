# https://docs.chainlit.io/get-started/pure-python

import chainlit as cl

from tutorials.openai_intro import response, client


@cl.on_message
async def main(message: cl.Message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with"
                                          "creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )


    await cl.Message(
        content=response.choices[0].message.content
    ).send()



if __name__ == "__main__":
    from chainlit.cli import run_chainlit
    run_chainlit("app.py")