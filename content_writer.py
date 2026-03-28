import json
import os
from datetime import datetime

def write_article():
    # Read keyword
    try:
        with open('trends.json', 'r') as f:
            trends = json.load(f)
        keyword = trends[0]['keyword']
    except:
        keyword = "best productivity software"
    
    # Create article content (no API needed - template-based)
    title = keyword.title() + " (2026): Top 5 Tools Compared"
    
    content = f"""# {title}

## Quick Comparison

| Tool | Price | Best For |
|------|-------|----------|
| Notion | $10/month | All-in-one workspace |
| ClickUp | $5/month | Task management |
| Monday | $8/month | Visual workflows |
| Asana | $11/month | Team collaboration |
| Trello | $5/month | Simple kanban |

## Winner: Notion

Notion remains the top choice for 2026. It combines notes, databases, and wikis in one flexible platform.

**Key Features:**
- Unlimited pages
- Database functionality  
- Templates gallery
- API access

[Try Notion Free](https://notion.so)

## Budget Pick: Trello

For those watching costs, Trello's free tier handles most small team needs.

## Buying Guide

When choosing {keyword}, look for:
1. Mobile app quality
2. Integration options
3. Export capabilities
4. Support response time

*Disclosure: We may earn a commission if you click our links at no extra cost to you.*

Published: {datetime.now().strftime('%B %d, %Y')}
"""
    
    # Save file
    os.makedirs('_posts', exist_ok=True)
    safe_name = keyword.replace(' ', '-').replace('/', '-')
    filename = f"_posts/{datetime.now().strftime('%Y-%m-%d')}-{safe_name}.md"
    
    # Add Jekyll header
    header = f"""---
layout: post
title: "{title}"
date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
---

"""
    
    with open(filename, 'w') as f:
        f.write(header + content)
    
    print(f"SUCCESS: Created {filename}")

if __name__ == "__main__":
    write_article()
    
