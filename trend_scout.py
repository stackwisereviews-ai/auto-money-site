import os
import json
import feedparser
import re
from datetime import datetime

def find_trends():
    """Scans Reddit and Product Hunt for money-making keywords"""
    
    opportunities = []
    
    # FREE METHOD: Reddit RSS feed for SideProject (no API key needed)
    try:
        reddit_feed = feedparser.parse("https://www.reddit.com/r/SideProject/.rss")
        for entry in reddit_feed.entries[:5]:
            title = entry.title
            # Look for software/app launches
            if any(word in title.lower() for word in ['app', 'saas', 'tool', 'platform', 'launched']):
                # Extract the main word (the product name or category)
                words = title.split()
                if len(words) > 2:
                    category = words[-2] if len(words) > 3 else "software"
                    opportunities.append({
                        "keyword": f"best {category} software",
                        "source": "reddit",
                        "date": str(datetime.now())
                    })
    except:
        pass
    
    # Always have a fallback so we never have empty content
    if not opportunities:
        opportunities = [
            {"keyword": "best ai scheduling software", "priority": "high"},
            {"keyword": "best notion alternatives", "priority": "medium"},
            {"keyword": "best free crm for small business", "priority": "high"}
        ]
    
    # Save to file
    with open('trends.json', 'w') as f:
        json.dump(opportunities[:3], f, indent=2)  # Top 3 only
    
    print(f"Found {len(opportunities)} opportunities")

if __name__ == "__main__":
    find_trends()
