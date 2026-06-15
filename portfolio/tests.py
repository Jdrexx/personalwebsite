from django.test import TestCase
from django.urls import reverse


class PortfolioPagesTests(TestCase):
    def test_home_page_loads_core_content(self):
        response = self.client.get(reverse('portfolio:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jonathan Dreksler')
        self.assertContains(response, 'Project Manager')
        self.assertContains(response, 'Image Placeholder')

    def test_projects_page_loads_github_projects(self):
        response = self.client.get(reverse('portfolio:projects'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ArchPlanReview')
        self.assertContains(response, 'ScanExcel')

    def test_resume_page_loads_resume_sections(self):
        response = self.client.get(reverse('portfolio:resume'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Vertical Visual Solutions')
        self.assertContains(response, 'Bachelor of Science in Computer Science')
