from django.test import TestCase
from .models import Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date

class GalleryModelsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Landscape")
        self.image_file = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        self.image = Image.objects.create(
            title="Sunset",
            image=self.image_file,
            created_date=date.today(),
            age_limit=12
        )
        self.image.categories.add(self.category)

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Landscape")

    def test_image_creation(self):
        self.assertEqual(self.image.title, "Sunset")
        self.assertEqual(self.image.age_limit, 12)
        self.assertIn(self.category, self.image.categories.all())
