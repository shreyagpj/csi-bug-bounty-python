"""
members.py
Manages library membership: registration, removal, lookup, and
overdue-fine calculation.
"""

from models import Member

FINE_PER_DAY = 5  # currency units charged per day a book is overdue


class MembershipManager:
    """Handles member registration and fine calculations."""

    def __init__(self):
        self.members = []

    def register_member(self, name):
        """Register a new member and assign them a unique member id."""
        new_id = len(self.members) + 1
        member = Member(new_id, name)
        self.members.append(member)
        return member

    def remove_member(self, member_id):
        self.members = [m for m in self.members if m.member_id != member_id]

    def find_member(self, member_id):
        for m in self.members:
            if m.member_id == member_id:
                return m
        return None

    def calculate_fine(self, days_overdue):
        """Calculate the total fine for a book returned late."""
        if days_overdue <= 0:
            return 0
        rate = FINE_PER_DAY
        total = days_overdue * FINE_PER_DAY
        return rate
