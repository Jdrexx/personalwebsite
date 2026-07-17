from django.test import TestCase
from django.urls import reverse


class PortfolioPagesTests(TestCase):
    def test_home_page_loads_core_content(self):
        response = self.client.get(reverse('portfolio:home'), secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jonathan Dreksler')
        self.assertContains(response, 'Project Manager')
        self.assertContains(response, 'Image Placeholder')

    def test_projects_page_loads_github_projects(self):
        response = self.client.get(reverse('portfolio:projects'), secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ArchPlanReview')
        self.assertContains(response, 'ScanExcel')

    def test_resume_page_loads_resume_sections(self):
        response = self.client.get(reverse('portfolio:resume'), secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Vertical Visual Solutions')
        self.assertContains(response, 'Bachelor of Science in Computer Science')

    def test_custom_404_page(self):
        response = self.client.get('/nonexistent-page/', secure=True)
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, 'Page not found', status_code=404)

    def test_custom_404_has_navigation(self):
        response = self.client.get('/does-not-exist/', secure=True)
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, 'Go Home', status_code=404)
