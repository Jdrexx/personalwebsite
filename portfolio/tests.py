from django.test import TestCase
from django.urls import reverse


class PortfolioPagesTests(TestCase):
    def test_home_page_loads_core_content(self):
        response = self.client.get(reverse('portfolio:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jonathan Dreksler')
        self.assertContains(response, 'Technical Project Manager')
        self.assertContains(response, 'degree and 4+ years')

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

    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:home'))
        self.assertTemplateUsed(response, 'portfolio/home.html')

    def test_projects_page_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:projects'))
        self.assertTemplateUsed(response, 'portfolio/projects.html')

    def test_resume_page_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:resume'))
        self.assertTemplateUsed(response, 'portfolio/resume.html')

    def test_urls_resolve_correctly(self):
        self.assertEqual(reverse('portfolio:home'), '/')
        self.assertEqual(reverse('portfolio:projects'), '/projects/')
        self.assertEqual(reverse('portfolio:resume'), '/resume/')
        self.assertEqual(reverse('portfolio:contact'), '/contact/')

    def test_contact_page_loads(self):
        response = self.client.get(reverse('portfolio:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Get in touch')

    def test_case_study_page_loads(self):
        response = self.client.get(reverse('portfolio:case_study', kwargs={'slug': 'knowledgeassistant'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'KnowledgeAssistant')
        self.assertContains(response, 'Case Study')

    def test_case_study_404_for_missing(self):
        response = self.client.get(reverse('portfolio:case_study', kwargs={'slug': 'nonexistent'}))
        self.assertEqual(response.status_code, 404)
