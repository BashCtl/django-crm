from django.test import TestCase

from ..models import Record


class ModelsTestCase(TestCase):

    def test_create_record_in_db(self):
        record = Record.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@test.com",
            phone="555-55-55",
            address="Wall St.",
            city="Dark",
            state="Sci-fi",
            zipcode="23456"
        )
        record.save()
        self.assertEqual(Record.objects.all().count(), 1)
