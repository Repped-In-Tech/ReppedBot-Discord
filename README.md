# ReppedBot - A Discord bot

ReppedBot chat bot built with Python. There are two scripts that can run, one is a generic Bot script that listens for events and commands, the other is a webhook that is scheduled to post a message every Monday, Wednesday and Friday at noon.

## Commands for the Bot
**These Are example commands to test if the bot works**

- `!hello`  - bot will respond with 'HEY'
- `!saymyname`  - bot will respond with 'what up `{your discord name}`'

When you join The server for the first time, you will receive a DM from ReppedBot welcoming you to the test server.

## To Test Locally

- ```shell 
  git clone git@github.com:Repped-In-Tech/ReppedBot-Discord.git
  ```
- Create a virtual environment

- ```shell
  pipenv install
  ```

- create a .env according to the sample env with [these](https://docs.google.com/spreadsheets/d/1IUZ4BoJgRJnbOfyMGNxHUXswgyZaCz1BD15bkJvQpi4/edit#gid=190460805) variables. If you don't have access to this sheet, get access from someone on the dev team with access.

#### To run the bot:

from the main directory:
`python main.py`

If you see this in your terminal, your bot is active:

![Terminal Message](https://res.cloudinary.com/dts9iifle/image/upload/v1712941707/Screen_Shot_2024-04-12_at_12.06.51_PM_bvv1fq.png)

Navigate to [Justin's Test Server](https://discord.gg/mhM4RjT9) and join to see the DM and interact with the bot with commands

#### To run the webhook:

from the main directory:
`python webhook.py`

You should see a message in the terminal that says, 'I am running'

You can test the standup messenger by changing the date times in `standups.py` to test the message

![Standup Test](https://res.cloudinary.com/dts9iifle/image/upload/v1712942360/Screen_Shot_2024-04-12_at_12.19.09_PM_vnukn1.png)
