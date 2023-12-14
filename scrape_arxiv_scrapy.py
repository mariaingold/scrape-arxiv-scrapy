# AROS v 0.1 (Academic Research Online System)
# Simple reflex agent web scraper
# Scrapes a specific arxiv page for basic citation data and stores in a CSV file
# Uses Python and Scrapy
#
# Author: Maria Ingold
# Built as part of UoEO MSc AI Intelligent Agents assignment

import scrapy

# To run this spider and output to a CSV, use the following command:
# scrapy runspider scrape_arxiv_scrapy.py -o citation_data_scrapy.csv

class ArxivSpider(scrapy.Spider):
    
    # COLLECT 

    # Unique identifier for the spider
    name = "arxiv" 

    # URLs to scrape
    start_urls = [
        "https://arxiv.org/abs/2109.00656", 
    ]

    # EXTRACT 

    # Parse the response object and extract the title, authors, and date of the paper
    def parse(self, response):
        citation_title = response.css('meta[name="citation_title"]::attr(content)').get(default="No meta title given")
        citation_authors = response.css('meta[name="citation_author"]::attr(content)').getall(default="No meta author given")
        citation_date = response.css('meta[name="citation_date"]::attr(content)').get(default="No meta date given")

        # TRANSFORM

        # Yield a dictionary with the values we want to export to a CSV file
        yield {
            "Title": citation_title,
            "Authors": "; ".join(citation_authors),
            "Date": citation_date,
        }

        # STORE
        # No need to store anything here since we are exporting to a CSV file using the -o option on the command line

        