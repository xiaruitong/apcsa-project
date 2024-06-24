# apcsa-project

Authors: Hebe, Helena, Cindy, Natalia

## About this Project

This project implemented a discord chat bot with a simple command-reply system, which is designed to help with rolling dice for TRPG players.

In this project, we utilized discord.py library to send HTTP requests to discord API, and handle the responses. Our contribution to this implementation is that we designed the application logic and defined the command systems, and deployed a working bot under the discord account of Hebe.

## Example `config.json`

This project relys on a `config.json` file at project root to start.

```json
{
  "discord" : {
    "token" : "<your-token-here>"
  },
  "proxy" : "<your-proxy-address-here>"
}
```