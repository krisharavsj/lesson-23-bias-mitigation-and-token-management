from hf import generate_response

def bias_mitigation_activity():
    print("\n=== BIAS MITIGATION ACTIVITY ===\n")
    prompt=input("Enter a prompt to run the activity.")
    if not prompt:
        print("Please enter a prompt to run the activity.")
        return
    initial_response=generate_response(prompt, temperature=0.3, max_tokens=1024)
    print(f"\nInitial AI response: {initial_response}")

    modified_prompt=input(
        "Modify the prompt to make it more neutral"
    ).strip()
    if modified_prompt:
        modified_prompt_response=modified_prompt(prompt, temperature=0.3, max_tokens=1024)
        print(f"\nInitial AI response: {modified_prompt}")
    else:
        print("no modified prompt")

def token_limit_activity():
    print("\n=== TOKEN LIMIT ACTIVITY ===\n")
    long_prompt=input("Enter a long prompt(300+ words) to run the activity.")
    if long_prompt:
        long_response=generate_response(long_prompt, temperature=0.3, max_tokens=1024)
        preview=(long_response[:500] + "...") if len(long_response)>500 else long_response
        print(f"response too long{preview}")
    else:
        print("No long prompt. skipping long prompt response. ")

    short_prompt=input("Enter a short prompt to run the activity.")
    if short_prompt:
        short_response=generate_response(short_prompt, temperature=0.3, max_tokens=1024)
        print(f"response too long{short_response}")
    else:
        print("No short prompt. skipping short prompt response. ")

def run_activity():
    print(f"\nAI learning activity")
    print("Choose an activity: ")
    print("1)Bias Mitigation")
    print("2)Token limits")
    choice=input("> ").strip()

    if choice=="1":
        bias_mitigation_activity()
    elif choice=="2":
        token_limit_activity()
    else:
        print("Invalid choice")

if __name__=="__main__":
    run_activity()