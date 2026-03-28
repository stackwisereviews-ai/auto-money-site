import os
import json
import requests
from datetime import datetime

def write_money_article(keyword):
    """Writes an affiliate article using Groq AI (no quota limits)"""
    
    api_key = os.environ.get('GROQ_API_KEY')
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    prompt = f"""Write a 1500-word SEO article titled: "{keyword.title()} (2026): Top 5 Tools Compared"

Structure:
1. Introduction: Acknowledge the reader's pain in choosing
2. Quick Comparison Table: 5 tools with pricing
3. Tool #1 (Winner): 300 words, mention "free trial available"
4. Tool #2 (Budget): 200 words on free/cheap option  
5. Tool #3 (Enterprise): 200 words for big teams
6. How We Tested: 100 words
7. Buying Guide: What features matter

Rules:
- Use markdown tables with |
- Never say "I think" or "In my opinion"
- Include dollar amounts ($10/month, etc.)
- End with: "Disclosure: We may earn a commission if you click our links at no extra cost to you."""

    data = {
        "model": "llama-3.1-8b-instant",  # Fast, free tier
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data
        )
        
        content = response.json()['choices'][0]['message']['content']
        
        # Create safe filename
        safe_name = keyword.replace(" ", "-").replace("/", "-")[:50]
        filename = f"_posts/{datetime.now().strftime('%Y-%m-%d')}-{safe_name}.md"
        
        # Add Jekyll frontmatter
        header = f"""---
layout: post
title: "{keyword.title()} (2026): Top 5 Tools Compared"
date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
categories: reviews
---

"""
        
        os.makedirs('_posts', exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(header + content)
        
        print(f"Created: {filename}")
        return filename
        
    except Exception as e:
        print(f"Error: {e}")
        print(f"Response: {response.text if 'response' in locals() else 'No response'}")
        return None

if __name__ == "__main__":
    try:
        with open('trends.json', 'r') as f:
            trends = json.load(f)
    except:
        trends = [{"keyword": "best ai writing software"}]
    
    if trends:
        write_money_article(trends[0]['keyword'])
        safe_name = keyword.replace(" ", "-").replace("/", "-")[:50]
        filename = f"_posts/{datetime.now().strftime('%Y-%m-%d')}-{safe_name}.md"
        
        # Add Jekyll frontmatter (tells website how to display it)
        header = f"""---
layout: post
title: "{keyword.title()} (2026): Top 5 Tools Compared"
date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
categories: reviews
---

"""
        
        # Save the article
        os.makedirs('_posts', exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(header + content)
        
        print(f"Created: {filename}")
        return filename
        
    except Exception as e:
        print(f"Error writing article: {e}")
        return None

if __name__ == "__main__":
    # Read what the scout found
    try:
        with open('trends.json', 'r') as f:
            trends = json.load(f)
    except:
        trends = [{"keyword": "best ai writing software"}]  # Fallback
    
    # Write article for the highest priority trend
    if trends:
        write_money_article(trends[0]['keyword'])
