from collections import deque

vip_line = deque()
normal_line = deque()

def new_ticket(ticket, priority="Normal"):
    if priority.lower() == "vip":
        vip_line.append(ticket)
        print(f"VIP ticket added: {ticket}")
    else:
        normal_line.append(ticket)
        print(f"Ticket added: {ticket}")

def process_ticket():
    if vip_line:
        done = vip_line.popleft()
        print(f"Processing VIP ticket: {done}")
    elif normal_line:
        done = normal_line.popleft()
        print(f"Processing ticket: {done}")
    else:
        print("No tickets to process!")

def peek_ticket():
    if vip_line:
        print(f"Next ticket: {vip_line[0]} (VIP)")
    elif normal_line:
        print(f"Next ticket: {normal_line[0]} (Normal)")
    else:
        print("No tickets in line.")

def show_tickets():
    print("\n--- Tickets in Line ---")
    if not vip_line and not normal_line:
        print("No tickets yet.")
    else:
        print("VIP tickets:")
        for i, t in enumerate(vip_line, 1):
            print(f"{i}. {t}")
        print("Normal tickets:")
        for i, t in enumerate(normal_line, 1):
            print(f"{i}. {t}")
    total = len(vip_line) + len(normal_line)
    print(f"\nTotal tickets: {total} | VIP: {len(vip_line)} | Normal: {len(normal_line)}")

def main():
    while True:
        print("\n--- Ticket Menu ---")
        print("1. New Ticket")
        print("2. Process Ticket")
        print("3. Peek Next Ticket")
        print("4. Show Tickets")
        print("5. Exit")

        choice = input("Choose (1-5): ")

        if choice == "1":
            ticket = input("Enter ticket name: ")
            priority = input("Enter priority (VIP/Normal): ")
            new_ticket(ticket, priority)

        elif choice == "2":
            process_ticket()

        elif choice == "3":
            peek_ticket()

        elif choice == "4":
            show_tickets()

        elif choice == "5":
            print("Closing ticket system. Bye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
