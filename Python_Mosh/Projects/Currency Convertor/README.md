## Features

- Converts amounts between USD, EUR, and CAD.
- Utilizes live exchange rates via the ForexRate API.
- Simple and interactive command-line interface.

## API Key Setup

To use the application, you need an API key for the ForexRate API. Follow these steps:

1. Obtain an API key from [ForexRate API](https://www.forexrateapi.com/).
2. Create a file named `api_key.py` in the project directory.
3. Add the following line to the file:
   ```python
   API_KEY = 'your_api_key_here'
   ```

## Example Usage

```bash
$ python app.py
Enter the amount: 100
Source currency (USD/EUR/CAD): USD
Target currency (USD/EUR/CAD): EUR
100.00 USD is equal to 92.50 EUR
```

## Troubleshooting

- **Invalid API Key**: Ensure your API key is correctly set in `api_key.py`.
- **Connection Issues**: Verify your internet connection.
- **Unsupported Currency**: Only USD, EUR, and CAD are supported.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
