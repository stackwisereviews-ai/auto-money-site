import json
from datetime import datetime

def find_trends():
    # Fallback articles that always work (no API needed)
    articles = [
        {"keyword": "best ai scheduling software", "priority": "high"},
        {"keyword": "best crm for small business", "priority": "high"},
        {"keyword": "best project management tool", "priority": "medium"}
    ]
    
    with open('trends.json', 'w') as f:
        json.dump(articles, f, indent=2)
    
    print("Trends saved")

if __name__ == "__main__":
    find_trends()
  
