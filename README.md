# X-Twitter-Clean

Automatically delete tweets and remove reposts from your X/Twitter account. This script uses Selenium to automate the process of cleaning up your X/Twitter timeline.

## Features
- Deletes tweets and removes reposts
- Works with the latest X/Twitter interface
- Handles rate limiting and dynamic loading
- Secure password input
- Automatic scrolling and content detection

## Prerequisites
- Python 3.6 or higher
- Chrome browser
- ChromeDriver matching your Chrome version

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/X-Twitter-Clean.git
cd X-Twitter-Clean
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Install ChromeDriver:
   - Download the version matching your Chrome browser from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)
   - Add it to your system PATH

## Usage

1. Run the script:
```bash
python twitter_delete.py
```

2. Enter your X/Twitter username when prompted
3. Enter your password (input will be hidden)
4. Let the script run - it will automatically scroll through your profile and remove tweets/reposts
5. Press Ctrl+C at any time to stop the script

## How It Works
- The script logs into your X/Twitter account using the provided credentials
- It scrolls through your profile, looking for tweets and reposts
- For each tweet found, it clicks the menu and delete buttons
- For each repost found, it clicks the repost button to undo it
- The script handles dynamic loading and rate limiting automatically

## Safety & Privacy
- Your password is never stored or logged
- The script runs in incognito mode
- No data is collected or transmitted except to X/Twitter
- All automation is done through official X/Twitter web interfaces

## Troubleshooting
- If the script fails to start, ensure ChromeDriver matches your Chrome version
- If login fails, check your credentials
- If the script seems stuck, try restarting it
- For other issues, check the error messages in the console

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer
This script is not affiliated with X/Twitter. Use at your own risk. The author is not responsible for any account restrictions or other consequences of using this script.
