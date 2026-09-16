"""
main.py
A small demo that exercises the Library Management System end to end.

Run it with:
    python main.py

Some of the printed results may look wrong. That's the point of
Bug Bounty -- read the output (and the code!) carefully.
"""

from datetime import timedelta

from inventory import Library
from members import MembershipManager
from transactions import TransactionManager


def main():
    library = Library()
    library.add_book("Clean Code", "Robert C. Martin", 2)
    library.add_book("The Hobbit", "J.R.R. Tolkien", 1)
    library.add_book("clean architecture", "Robert C. Martin", 1)

    members = MembershipManager()
    alice = members.register_member("Alice")
    bob = members.register_member("Bob")

    transactions = TransactionManager(library, members)

    print("=== Searching the catalog for 'Clean' ===")
    print(library.search_by_title("Clean"))
    print("(Expected: both 'Clean Code' AND 'clean architecture')\n")

    print("=== Borrowing books ===")
    print("Alice borrows 'Clean Code':", transactions.borrow_book(alice.member_id, 1))
    print("Bob borrows 'The Hobbit':", transactions.borrow_book(bob.member_id, 2))

    print("\n=== Alice tries to borrow 'The Hobbit' too (0 copies left) ===")
    result = transactions.borrow_book(alice.member_id, 2)
    print("Borrow succeeded?:", result, "(expected: False)")
    print("'The Hobbit' available_copies now:", library.find_book_by_id(2).available_copies)

    print("\n=== Member borrowed-book lists ===")
    print("Alice's borrowed books:", alice.borrowed_books)
    print("Bob's borrowed books:", bob.borrowed_books)
    print("(Expected: each member should only see their OWN borrowed books)")

    print("\n=== Direct fine check: 6 days overdue ===")
    print("calculate_fine(6):", members.calculate_fine(6), "(expected: 30)")

    print("\n=== Simulating Bob returning 'The Hobbit' 6 days late ===")
    bob_record = next(
        r for r in transactions.transaction_log
        if r["member_id"] == bob.member_id and r["book_id"] == 2
    )
    bob_record["due_date"] -= timedelta(days=20)  # pretend the due date already passed
    fine = transactions.return_book(bob.member_id, 2)
    print("Fine charged to Bob:", fine, "(expected: a positive fine, not 0)")

    print("\n=== Removing Alice, then registering a new member Carol ===")
    members.remove_member(alice.member_id)
    carol = members.register_member("Carol")
    print("Bob's member id:", bob.member_id)
    print("Carol's member id:", carol.member_id, "(expected: different from Bob's)")

    print("\n=== A second, unrelated library branch ===")
    branch = Library()
    branch.add_book("Clean Coding Handbook", "Someone Else", 3)
    print("branch search for 'Clean':", branch.search_by_title("Clean"))
    print("(Expected: only 'Clean Coding Handbook', not books from the first library)")


if __name__ == "__main__":
    main()
