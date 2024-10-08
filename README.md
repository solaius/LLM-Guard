# LLM-Guard

LLM-Guard is a Python-based prototype designed to interact with large language models (LLMs) like Mistral and Granite through APIs. The main goal is to test and evaluate prompts for toxicity, prompt injection, and other security concerns using LLM Guard, LangChain, and custom input/output scanners.

## Features

- Integration with Mistral and Granite LLMs.
- Scans prompts for toxicity, data leakage, prompt injection, and other risks.
- Uses `LLMGuard` for automated prompt and response scanning.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/solaius/LLM-Guard.git
   cd LLM-Guard
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory to store your API keys and model names:

   ```
   MISTRAL_API_URL=<your_mistral_api_url>
   MISTRAL_API_KEY=<your_mistral_api_key>
   MISTRAL_MODEL_NAME=<your_mistral_model_name>
   
   ```

## Usage

Run the `main.py` file to test prompts using LLM-Guard:

```bash
python main.py
```

The script scans a set of predefined prompts for issues like toxicity and prompt injection using the specified LLM. It returns sanitized results and highlights any flagged prompts.

## Dependencies

- Python 3.8+
- [LangChain](https://python.langchain.com/)
- [LLM Guard](https://llm-guard.com/)
- httpx
- dotenv

## Contributing

Feel free to open issues and submit pull requests. For major changes, please open an issue to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For further questions, please contact [solaius](https://github.com/solaius).