from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import time
from agents.web_lookup_agent import lookup as web_lookup_agent
from decouple import config


def split_text(text, chunk_size):
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]


def main():
    summary_template = """
    Bir kişi hakkında verilen {information} göz önünde bulundurarak:
    1. Kişinin profesyonel ve kişisel yönlerini vurgulayan kısa ve kapsamlı bir özet oluşturun.
    2. Kişiyle ilgili iki ilginç gerçeği belirleyin.
    3. Kariyeri, başarıları veya sosyal medya varlığı hakkında içgörüler sağlayın.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    name = input('Aramak istediğin ismi yaz:')

    data = web_lookup_agent(name=name)

    chunk_size = 1000
    chunks = split_text(data, chunk_size)

    llm = ChatOpenAI(api_key=config("OPENAI_API_KEY"), temperature=0, model_name="gpt-3.5-turbo-16k")

    for chunk in chunks:
        chain = LLMChain(llm=llm, prompt=summary_prompt_template)
        result = chain.run(information=chunk)
        print(result)

        time.sleep(30)


if __name__ == "__main__":
    main()
