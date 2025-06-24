def send_targets(targets):
    print("Selected targets to send (AOCS positions):")
    for digit, aocs in targets.items():
        print(f"Digit: {digit}, AOCS: {aocs}")