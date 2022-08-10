"""Tests all models."""
from django.test import TestCase
from core.models import Student


class StudentTest(TestCase):
    """ Test module for Student model."""

    def setUp(self):
        Student.objects.create(name='John', code='S10')
        Student.objects.create(name='Rufus', code='S11')

    def test_student_str(self):
        student = Student.objects.get(code='S10')
        self.assertEqual(student.__str__(), 'John - S10')
