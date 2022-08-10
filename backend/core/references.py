"""References."""


class StudentState(object):
    """States for student."""

    ACTIVE = 'active'
    INACTIVE = 'inactive'

    STUDENT_STATE_REFERENCE = {
        ACTIVE: 'Active',
        INACTIVE: 'Inactive',
    }

    STUDENT_STATE_CHOICES = tuple(STUDENT_STATE_REFERENCE.items())
