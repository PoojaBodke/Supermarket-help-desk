"""
Supermarket Help Desk Chatbot (Menu-based, with emojis)
Author: [Your Name]
Description:
    A simple Python chatbot where the customer selects help topics by number,
    now with emojis for a friendlier interface.
"""

# Dictionary mapping option numbers to topics and responses
help_options = {
    '1': ('🕒 Store Hours', 'Our typical store hours are 7 AM to 11 PM, but please check your local store page for exact hours.'),
    '2': ('📦 Order Status', 'You can track your order status in your Supermarket account under "Purchase History."'),
    '3': ('❌ Cancel Order', 'To cancel an order, go to your Supermarket account > Purchase History > Cancel, if the option is available.'),
    '4': ('🔄 Return Policy', 'Most items can be returned within 90 days with a receipt. Some exceptions apply.'),
    '5': ('💰 Refund', 'Refunds are usually processed within 5-7 business days after the item is received at our warehouse.'),
    '6': ('🚚 Delivery Time', 'Standard delivery takes 3-5 business days. Same-day and next-day delivery may be available in your area.'),
    '7': ('⭐ Membership', 'Supermarket+ members get free shipping, discounts on fuel, and more for $12.95/month or $98/year.'),
    '8': ('💳 Payment Methods', 'We accept Visa, MasterCard, American Express, Discover, Supermarket gift cards, and PayPal.')
}

def show_menu():
    print("\n🤖 How can I help you today? Please choose an option:")
    for number, (topic, _) in help_options.items():
        print(f"{number}. {topic}")
    print("✏️ Type 'bye', 'exit', or 'quit' to end the chat.")

def get_response(user_choice):
    if user_choice in help_options:
        _, response = help_options[user_choice]
        return response
    else:
        return "⚠️ Sorry, I didn't understand that option. Please choose a valid number from the menu."

def main():
    print("👋 Hello! Welcome to Supermarket Help Desk Chatbot.")
    while True:
        show_menu()
        user_input = input("\nYour choice: ").strip().lower()

        if user_input in ['bye', 'exit', 'quit']:
            print("👋 Bot: Thank you for visiting Supermarket Help Desk. Goodbye!")
            break

        response = get_response(user_input)
        print(f"🤖 Bot: {response}")

if __name__ == "__main__":
    main()
