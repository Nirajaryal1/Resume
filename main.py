import argparse
from crawler import Crawler
from downloader import Downloader

def main():
    parser = argparse.ArgumentParser(description="Meme Downloader for indianmemetemplates.com")
    parser.add_argument("--url", type=str, default="https://indianmemetemplates.com/category/videos/", 
                        help="Starting category URL (default: /category/videos/)")
    parser.add_argument("--pages", type=int, default=1, help="Number of pages to scrape (default: 1)")
    args = parser.parse_args()

    crawler = Crawler()
    downloader = Downloader()

    current_url = args.url
    pages_processed = 0

    while current_url and pages_processed < args.pages:
        print(f"\n--- Scraping Page {pages_processed + 1}: {current_url} ---")
        soup = crawler.get_soup(current_url)
        if not soup:
            break

        post_links = crawler.extract_memes_from_page(soup)
        print(f"Found {len(post_links)} memes on this page.")

        for post_url in post_links:
            print(f"Processing post: {post_url}")
            img_url, vid_url = crawler.extract_media_from_post(post_url)
            
            if vid_url:
                downloader.download_file(vid_url, folder_type="videos")
            if img_url:
                downloader.download_file(img_url, folder_type="images")

        pages_processed += 1
        current_url = crawler.get_next_page(soup)
        
        if not current_url:
            print("No more pages found.")

    print("\nDownload process completed.")

if __name__ == "__main__":
    main()
