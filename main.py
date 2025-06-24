from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
import os

load_dotenv()


#getting api key
API_KEY = os .getenv('Gemini_API_key')
print(API_KEY)


#Error if API KEY mssing
if not API_KEY:
    raise ValueError("API_KEY is not set. Please set it in the .env file.")

#  Setup external OpenAI-compatible client (Gemini)
client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#  Configure model
model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=client
)

#  Configuration
config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

#create agent


agent=Agent(
    name="Translator",
    instructions="""You are a translator of all languages .""",
)


response = Runner.run_sync(
    agent,
    "Hello, how are you? translate this to german",
    run_config=config
)


print(response.final_output)