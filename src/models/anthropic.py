from langchain_anthropic import ChatAnthropic
model = ChatAnthropic(model_name='claude-3-opus-20240229', timeout=60, stop=None)