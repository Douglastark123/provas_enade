from openai import OpenAI
from dotenv import load_dotenv
from args_parser import args_parser
from extract_pdf import extract_pdf_text

def main():
  load_dotenv()
  file = args_parser()
  print(file)
  output = extract_pdf_text(file)
  print(output)
  # client = OpenAI()
  # client.api_key = os.getenv("OPEN_API_KEY")
  # response = client.responses.create(
  #   model="gpt-4o",
  #   input= "Write a one-sentence bedtime story about a unicorn."
  # )

  # print(response.output_text)


if __name__ == "__main__":
    main()