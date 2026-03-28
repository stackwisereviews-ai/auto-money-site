import os
import json
import google.generativeai as genai
from datetime import datetime

# Set up the AI brain (uses your free secret key)
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.0-flash')

def write_money_article(keyword):
    """Writes an affiliate article designed to make money"""
    
    prompt = f"""
    Write a 1500-word SEO article titled: "{keyword.title()} (2026): Top 5 Tools Compared"
    
    Structure:
    1. Introduction: Acknowledge the reader's pain in choosing (analysis paralysis)
    2. Quick Comparison Table: 5 tools with pricing, best for, and one-line verdict
    3. Tool #1 (The Winner): 300 words on the best option. Mention "free trial available" naturally.
    4. Tool #2 (Budget Pick): 200 words on free/cheap alternative
    5. Tool #3 (Enterprise): 200 words for big teams
    6. How We Tested: 100 words adding credibility
    7. Buying Guide: What features actually matter (not fluff)
    
    Rules:
    - Use comparison tables with | symbols for markdown
    - Never say "I think" or "In my opinion". State facts.
    - Include specific dollar amounts in pricing ($10/month, etc.)
    - End with: "Disclosure: We may earn a commission if you click our links at no extra cost to you."
    """
    
    try:
        response = model.generate_content(prompt)
        content = response.text
        
        # Create safe filename from keyword
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
