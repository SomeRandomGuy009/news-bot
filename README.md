# news-bot / News article scraper
implement what this video says https://www.youtube.com/watch?v=BVizDqOfins

A simple script that uses the `requests` and `newspaper3k` libraries to scrape the top headline from [Google News](https://news.google.com/) and extract the text and summary of the article. The article text and summary are then saved to `article.txt` and `summary.txt` respectively.

## Requirements
- Python 3
- requests
- newspaper3k
- json
- API key from [NewsAPI](https://newsapi.org/)

## Usage
1. Clone the repository
2. `pip install -r requirements.txt`
3. Put NewsAPI api key in main.py file.
4. Run the script using `python main.py`

## License
This project is licensed under the MIT License, which means you can use, modify, and distribute the code as long as you give credit to the original author. See the [LICENSE](LICENSE) file for more details.

## Contributing
Open a PR or an Issue for contribution.

## TODO:
- implement whatever is left in the video:
     1. Use pyttsx3 or any other text to speech service to make the audio.
     2. Use newspaper3k module's newspaper.keywords to get the keywords of the article and find a relevant video to use.
     
## Credits
Thanks to 1. ChatGPT for helping me generate this README.<br>
          2. [CodeWithLewis](https://www.youtube.com/watch?v=BVizDqOfins) for giving this idea
