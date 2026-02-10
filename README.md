# vigilant-octo-broccoli
Introducing Google's ADK Framework

<p align="center">
    <img src="./images/adk.png" height="400">
</p>

This article is a companion repository to the Medium article [📱Would you like an app with that? — Introducing the ADK Framework](https://medium.com/@tituslhy/would-you-like-an-app-with-that-introducing-the-adk-framework-aead05a8b9cd?postPublishedType=initial)

## To run remote A2A services:
```
cd app

uvicorn assistant.remotes.exchange_rate_agent.agent:a2a_currency_app --host localhost --port 8001

uvicorn assistant.remotes.get_weather_agent.agent:a2a_weather_app --host localhost --port 8002
```

## To spin up the app
```
cd app

adk web --port 8000
```

## To spin up the app in backend version
```
cd app

adk api_server
```

## To create a new agent using ADK
```
adk create <your_agent_name>
```