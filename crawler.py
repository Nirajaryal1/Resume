import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class Crawler:
    def __init__(self, base_url="https://indianmemetemplates.com/"):
        self.base_url = base_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def get_soup(self, url):
        try:
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

    def extract_memes_from_page(self, soup):
        """
        Extracts list of post detail pages from a category/home page.
        """
        meme_links = []
        # Target article tags or links with specific patterns
        articles = soup.select('article.ast-article-post')
        for article in articles:
            link = article.select_one('h2.entry-title a') or article.select_one('a')
            if link and link.get('href'):
                meme_links.append(link.get('href'))
        return meme_links

    def extract_media_from_post(self, post_url):
        """
        Extracts direct image and video URLs from a single meme post page.
        """
        soup = self.get_soup(post_url)
        if not soup:
            return None, None

        image_url = None
        video_url = None

        # Check for Video
        video_tag = soup.select_one('video')
        if video_tag:
            # Check for src attribute on video tag itself
            video_url = video_tag.get('src')
            if not video_url:
                # Check for source tags
                source_tag = video_tag.select_one('source')
                if source_tag:
                    video_url = source_tag.get('src')
        
        # If no video source, try searching for other video embeds or iframes if necessary
        # But based on research, <video> is the main way.

        # Check for Image
        # Look for the main image in the entry-content
        img_tag = soup.select_one('div.entry-content img')
        if img_tag:
            # Prefer 'src' but check 'data-src' for lazy loading
            image_url = img_tag.get('src') or img_tag.get('data-src')

        return image_url, video_url

    def get_next_page(self, soup):
        """
        Finds the 'Next' page link from the pagination.
        """
        next_link = soup.select_one('.next.page-numbers')
        if next_link and next_link.get('href'):
            return next_link.get('href')
        return None
