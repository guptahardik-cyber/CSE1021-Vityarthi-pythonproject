import os

candidates = ["candidate-1", "candidate-2", "candidate-3"]
votes = {name: 0 for name in candidates}
voted_ids = [] 



def show_menu():
    print("\n===== DIGITAL VOTING SYSTEM =====")
    print("1. View candidates")
    print("2. Cast a vote")
    print("3. View live results")
    print("4. Save results to file")
    print("5. Exit")


def show_candidates():
    print("\nCandidates:")
    for i, name in enumerate(candidates, start=1):
        print(f"  {i}. {name}")


def cast_vote():
    voter_id = input("Enter your voter ID (e.g. reg number): ").strip()

    if voter_id == "":
        print("Voter ID cannot be empty.")
        return

    if voter_id in voted_ids:
        print("You have already voted! Only one vote per person is allowed.")
        return

    show_candidates()
    choice = input("Enter the number of the candidate you want to vote for: ").strip()

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    choice = int(choice)
    if choice < 1 or choice > len(candidates):
        print("That candidate number doesn't exist.")
        return

    chosen_candidate = candidates[choice - 1]
    votes[chosen_candidate] += 1
    voted_ids.append(voter_id)
    print(f"Vote recorded for {chosen_candidate}. Thank you for voting!")


def show_results():
    print("\n----- LIVE RESULTS -----")
    total_votes = sum(votes.values())
    if total_votes == 0:
        print("No votes cast yet.")
        return

   
    sorted_votes = sorted(votes.items(), key=lambda item: item[1], reverse=True)

    for name, count in sorted_votes:
        percentage = (count / total_votes) * 100
        bar = "#" * count  # simple visual bar
        print(f"{name:10s} | {count:3d} votes ({percentage:5.1f}%) {bar}")

    print(f"\nTotal votes cast: {total_votes}")

    winner, winning_count = sorted_votes[0]
    if winning_count > 0:
        print(f"Current leader: {winner}")


def save_results():
    filename = "voting_results.txt"
    with open (filename, "w") as f:
        f.write("DIGITAL VOTING SYSTEM - FINAL RESULTS\n")
        f.write("=" * 40 + "\n")
        total_votes = sum(votes.values())
        for name, count in sorted(votes.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total_votes * 100) if total_votes else 0
            f.write(f"{name}: {count} votes ({percentage:.1f}%)\n")
        f.write(f"\nTotal votes: {total_votes}\n")

    full_path = os.path.abspath(filename)
    print(f"Results saved to {full_path}")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_candidates()
        elif choice == "2":
            cast_vote()
        elif choice == "3":
            show_results()
        elif choice == "4":
            save_results()
        elif choice == "5":
            print("Exiting voting system. Goodbye!")
            break
        else:
            print("Invalid option, please choose 1-5.")


if __name__ == "__main__":
    main()