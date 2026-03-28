import os
import json
import requests
from datetime import datetime

def write_money_article(keyword):
    """Writes an affiliate article using Groq AI"""
    
    api_key = os.environ.get('GROQ_API_KEY')
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    prompt = f"""Write a 1500-word SEO article titled: "{keyword.title()} (2026): Top 5 Tools Compared"

Structure:
1. Introduction: Acknowledge reader's pain in choosing software
2. Comparison Table: 5 tools with pricing, best for, verdict
3. Tool #1 (Winner): 300 words, mention "free trial available"
4. Tool #2 (Budget): 200 words on cheap alternative
5. Tool #3 (Enterprise): 200 words for big teams
6. How We Tested: 100 words
7. Buying Guide: What features matter

Rules:
- Use markdown tables
- No "I think" or opinions, state facts
- Include dollar amounts ($10/month)
- End with: "Disclosure: We may earn a commission if you click our links."""

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        content = response.json()['choices'][0]['message']['content']
        
        # Create filename
        safe_name = keyword.replace(" ", "-").replace("/", "-")[:50]
        filename = f"_posts/{datetime.now().strftime('%Y-%m-%d')}-{safe_name}.md"
        
        # Jekyll frontmatter
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
        
        print(f"SUCCESS: Created {filename}")
        return filename
        
    except Exception as e:
        print(f"ERROR: {e}")
        return None

if __name__ == "__main__":
    try:
        with open('trends.json', 'r') as f:
            trends = json.load(f)
    except:
        trends = [{"keyword": "best ai writing software"}]
    
    if trends:
        result = write_money_article(trends[0]['keyword'])
        if result:
            print("Article written successfully")
        else:
            print("Failed to write article")
