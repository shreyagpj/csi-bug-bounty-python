"""
transactions.py
Handles borrowing and returning books, due dates, fine calculation,
and monthly transaction reporting.
"""

from datetime import datetime, timedelta

LOAN_PERIOD_DAYS = 14


class TransactionManager:
    """Tracks borrow/return transactions for the library."""

    def __init__(self, library, membership_manager):
        self.library = library
        self.membership_manager = membership_manager
        # Each record: {member_id, book_id, borrow_date, due_date, return_date}
        self.transaction_log = []

    def borrow_book(self, member_id, book_id):
        member = self.membership_manager.find_member(member_id)
        book = self.library.find_book_by_id(book_id)

        if member is None or book is None:
            return False
        if not self.library.is_available(book_id):
            return False

        borrow_date = datetime.now()
        due_date = borrow_date + timedelta(days=LOAN_PERIOD_DAYS)

        record = {
            "member_id": member_id,
            "book_id": book_id,
            "borrow_date": borrow_date,
            "due_date": due_date,
            "return_date": None,
        }
        self.transaction_log.append(record)

        member.borrowed_books.append(book_id)
        book.available_copies -= 1
        return True

    def return_book(self, member_id, book_id):
        record = self._find_open_record(member_id, book_id)
        if record is None:
            return None

        record["return_date"] = datetime.now()

        member = self.membership_manager.find_member(member_id)
        book = self.library.find_book_by_id(book_id)

        if book_id in member.borrowed_books:
            member.borrowed_books.remove(book_id)
        book.available_copies += 1

        days_overdue = (record["due_date"].date() - record["return_date"].date()).days
        fine = self.membership_manager.calculate_fine(days_overdue)
        return fine

    def _find_open_record(self, member_id, book_id):
        for record in self.transaction_log:
            if (record["member_id"] == member_id
                    and record["book_id"] == book_id
                    and record["return_date"] is None):
                return record
        return None

    def is_book_returned(self, member_id, book_id):
        """Check whether a specific borrowed book has already been returned."""
        record = self._find_open_record(member_id, book_id)
        return record is not None

    def generate_monthly_report(self):
        """Snapshot current transactions into a report, then clear the log
        so next month starts fresh."""
        report = {
            "generated_on": datetime.now(),
            "transactions": self.transaction_log,
        }
        self.transaction_log.clear()
        return report
