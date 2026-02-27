import os
from agent import graph

def run_test():
    print("🚀 Starting Visual LangGraph Test Run...")
    
    # A realistic sample product profile
    state = {
        "product": {
            "title": "MyFreedomBot Masterclass",
            "type": "Course",
            "id": "myfreedombot-demo",
            "shortDescription": "A transformative 2-hour masterclass teaching Gen-X women how to build their first personal AI assistant without coding.",
            "detailedDescription": "This masterclass takes you step-by-step through setting up MyFreedomBot. It covers creating a Telegram bot, linking it to the Claude and GPT APIs, setting up a database for memory, and configuring proactive check-ins. Designed for beginners who want to reclaim their time and energy using AI."
        },
        "templates": [
            {
                "id": "sales_page",
                "name": "Sales Page Copy",
                "template": "Write a high-converting, empathetic Sales Page for {{PRODUCT_TITLE}}. Type: {{PRODUCT_TYPE}}. Hook the reader with Truth. Describe how it will positively impact their Time, Energy, Money, and Happiness. Use Markdown. Short desc: {{SHORT_DESCRIPTION}}. Long desc: {{DETAILED_DESCRIPTION}}."
            },
            {
                "id": "ad_copy",
                "name": "Facebook Ad",
                "template": "Write engaging Facebook Ad copy for {{PRODUCT_TITLE}}. Focus on reclaiming Time and Happiness. Short desc: {{SHORT_DESCRIPTION}}."
            },
            {
                "id": "welcome_email",
                "name": "Welcome Sequence",
                "template": "Write the Welcome Email for new students of {{PRODUCT_TITLE}}. Set expectations and congratulate them. Markdown format. Short desc: {{SHORT_DESCRIPTION}}."
            }
        ]
    }
    
    try:
        # Run the compiled LangGraph directly!
        result = graph.invoke(state)
        
        print("\n✅ Visual Pipeline Completed Successfully!")
        print("Final HTML Aggregator Output Path:")
        print(result.get("final_output_path", "N/A"))
        print("\nTest completed. Check the generated directory!")
        
    except Exception as e:
        print(f"Error executing LangGraph pipeline: {e}")

if __name__ == "__main__":
    run_test()
