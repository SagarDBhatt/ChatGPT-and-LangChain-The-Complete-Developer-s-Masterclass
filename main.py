
endpoint_url = "https://geicoopenainp01.openai.azure.com/"
api_version = "2024-08-01-preview"
gpt_temprature = 0.0
gpt_n=1
deployment_name = "TeleComDocSummarizeGPT4gpt-4o-2024-08-06"

import openai
import asyncio

client = openai.AzureOpenAI(
    azure_endpoint=endpoint_url,
    api_version=api_version,
    api_key=api_key,
    max_retries=3
)

async_client = openai.AsyncAzureOpenAI(
    azure_endpoint=endpoint_url,
    api_version=api_version,
    api_key=api_key,
    max_retries=3
)

async def get_completion():
    result = await async_client.beta.chat.completions.parse(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France? Respond in JSON format with a key 'capital'."}
        ],
        max_tokens=100,
        n=gpt_n,
        temperature=gpt_temprature,
        response_format={"type": "json_object"}
    )
    print("Printing the LLM response:")
    print(result.choices[0].message.content)
          

#RUN the async function
asyncio.run(get_completion())