import json
import re

from django.test import TestCase
from django.urls import reverse

from .content import SITE_CONTENT
from .services import SERVICES


class PortfolioPagesTests(TestCase):
    def test_home_page_loads_core_content(self):
        response = self.client.get(reverse('portfolio:home'), secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jonathan Dreksler')
        self.assertContains(response, 'Websites and AI automation built around your business')
        self.assertContains(response, 'a real person who answers')

    def test_home_typewriter_reserves_layout_and_remains_accessible(self):
        response = self.client.get(reverse('portfolio:home'), secure=True)
        self.assertContains(response, 'class="typewriter-sizer" aria-hidden="true"')
        self.assertContains(response, 'class="typewriter-animated" aria-hidden="true"')
        self.assertContains(response, 'class="sr-only"')

    def test_home_uses_responsive_featured_image(self):
        response = self.client.get(reverse('portfolio:home'), secure=True)
        self.assertContains(response, 'featured-work-480.webp')
        self.assertContains(response, 'featured-work-720.webp')
        self.assertContains(response, 'featured-work-960.webp')
        self.assertContains(response, 'featured-work-480.avif')
        self.assertContains(response, 'featured-work-720.avif')
        self.assertContains(response, 'featured-work-960.avif')
        self.assertContains(response, 'type="image/avif"')
        self.assertContains(response, 'type="image/webp"')

    def test_brand_uses_visible_text_as_accessible_name(self):
        response = self.client.get(reverse('portfolio:home'), secure=True)
        self.assertNotContains(response, 'aria-label="Jonathan Dreksler home"')

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

    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:home'), secure=True)
        self.assertTemplateUsed(response, 'portfolio/home.html')

    def test_projects_page_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:projects'), secure=True)
        self.assertTemplateUsed(response, 'portfolio/projects.html')

    def test_resume_page_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:resume'), secure=True)
        self.assertTemplateUsed(response, 'portfolio/resume.html')

    def test_urls_resolve_correctly(self):
        self.assertEqual(reverse('portfolio:home'), '/')
        self.assertEqual(reverse('portfolio:projects'), '/projects/')
        self.assertEqual(reverse('portfolio:resume'), '/resume/')
        self.assertEqual(reverse('portfolio:contact'), '/contact/')

    def test_contact_page_loads(self):
        response = self.client.get(reverse('portfolio:contact'), secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Get in touch')

    def test_case_study_page_loads(self):
        response = self.client.get(reverse('portfolio:case_study', kwargs={'slug': 'knowledgeassistant'}), secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'KnowledgeAssistant')
        self.assertContains(response, 'Case Study')

    def test_case_study_404_for_missing(self):
        response = self.client.get(reverse('portfolio:case_study', kwargs={'slug': 'nonexistent'}), secure=True)
        self.assertEqual(response.status_code, 404)

    def test_case_study_hyphenated_variant_redirects_to_canonical(self):
        response = self.client.get('/case-study/arch-plan-review/', secure=True)
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response['Location'], '/case-study/archplanreview/')

    def test_case_study_mixed_case_variant_redirects_to_canonical(self):
        response = self.client.get('/case-study/ArchPlanReview/', secure=True)
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response['Location'], '/case-study/archplanreview/')

    def test_case_study_canonical_slug_serves_200(self):
        response = self.client.get('/case-study/archplanreview/', secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'rel="canonical" href="https://jdreksler.com/case-study/archplanreview/"')

    def test_legacy_urls_permanently_redirect(self):
        expected = {
            '/index.html': '/',
            '/portfolio/': '/projects/',
            '/about/': '/',
            '/blog/': '/',
            '/hire-me/': '/contact/',
        }
        for old, target in expected.items():
            with self.subTest(old=old):
                response = self.client.get(old, secure=True)
                self.assertEqual(response.status_code, 301)
                self.assertEqual(response['Location'], target)

    def test_home_links_directly_to_case_studies(self):
        response = self.client.get(reverse('portfolio:home'), secure=True)
        self.assertContains(response, 'featured-case-links')
        self.assertContains(response, '/case-study/scanexcel/')
        self.assertContains(response, '/case-study/knowledgeassistant/')
        self.assertContains(response, '/case-study/jobcrm/')

    def test_thanks_page_loads(self):
        response = self.client.get(reverse('portfolio:thanks'), secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Thanks for reaching out')

    def test_custom_404_page(self):
        response = self.client.get('/nonexistent-page/', secure=True)
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, 'Page not found', status_code=404)

    def test_custom_404_has_navigation(self):
        response = self.client.get('/does-not-exist/', secure=True)
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, 'Back to home', status_code=404)


class SeoInfrastructureTests(TestCase):
    def setUp(self):
        self.indexable_routes = [
            reverse('portfolio:home'),
            reverse('portfolio:services'),
            reverse('portfolio:projects'),
            reverse('portfolio:resume'),
            reverse('portfolio:contact'),
            *[
                reverse('portfolio:service_detail', kwargs={'slug': slug})
                for slug in SERVICES
            ],
            *[
                reverse('portfolio:case_study', kwargs={'slug': project['name'].lower()})
                for project in SITE_CONTENT['projects']
                if project.get('case_study')
            ],
        ]

    def test_every_indexable_page_has_unique_complete_metadata(self):
        titles = set()
        canonicals = set()
        for route in self.indexable_routes:
            with self.subTest(route=route):
                response = self.client.get(route, secure=True)
                self.assertEqual(response.status_code, 200)
                html = response.content.decode()
                title = re.search(r'<title>(.*?)</title>', html).group(1)
                canonical = re.search(r'<link rel="canonical" href="([^"]+)"', html).group(1)
                description = re.search(r'<meta name="description" content="([^"]+)"', html).group(1)
                self.assertTrue(title.strip())
                self.assertGreaterEqual(len(description), 80)
                # Concise descriptions are less likely to be truncated in search
                # results and social previews.
                self.assertLessEqual(len(description), 160)
                self.assertTrue(canonical.startswith('https://jdreksler.com/'))
                self.assertIn('<meta name="robots" content="index,follow,max-image-preview:large">', html)
                self.assertIn('<meta property="og:url" content="', html)
                self.assertIn('<meta name="twitter:image:alt" content="', html)
                self.assertNotIn(title, titles)
                self.assertNotIn(canonical, canonicals)
                titles.add(title)
                canonicals.add(canonical)

    def test_json_ld_is_server_rendered_and_valid(self):
        routes = [
            reverse('portfolio:home'),
            reverse('portfolio:projects'),
            reverse('portfolio:service_detail', kwargs={'slug': 'ai-workflow-automation'}),
            reverse('portfolio:case_study', kwargs={'slug': 'knowledgeassistant'}),
        ]
        for route in routes:
            with self.subTest(route=route):
                html = self.client.get(route, secure=True).content.decode()
                match = re.search(r'<script type="application/ld\+json">(.*?)</script>', html)
                self.assertIsNotNone(match)
                payload = json.loads(match.group(1))
                self.assertEqual(payload['@context'], 'https://schema.org')
                self.assertGreaterEqual(len(payload['@graph']), 2)

    def test_case_studies_have_article_and_breadcrumb_schema(self):
        response = self.client.get(
            reverse('portfolio:case_study', kwargs={'slug': 'scanexcel'}), secure=True
        )
        self.assertContains(response, '"@type":"TechArticle"')
        self.assertContains(response, '"@type":"BreadcrumbList"')
        self.assertContains(response, 'og:type" content="article"')

    def test_service_pages_have_service_schema_and_internal_links(self):
        for slug, service in SERVICES.items():
            with self.subTest(slug=slug):
                response = self.client.get(
                    reverse('portfolio:service_detail', kwargs={'slug': slug}), secure=True
                )
                self.assertContains(response, service['name'])
                self.assertContains(response, '"@type":"Service"')
                for project_name in service['related']:
                    self.assertContains(response, project_name)

    def test_sitemap_contains_all_indexable_pages_only(self):
        response = self.client.get('/sitemap.xml', secure=True)
        self.assertEqual(response.status_code, 200)
        xml = response.content.decode()
        for route in self.indexable_routes:
            self.assertIn(f'https://jdreksler.com{route}', xml)
        self.assertNotIn('/thanks/', xml)
        self.assertEqual(xml.count('<url>'), len(self.indexable_routes))

    def test_robots_allows_public_site_and_declares_sitemap(self):
        response = self.client.get('/robots.txt', secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/plain; charset=utf-8')
        self.assertContains(response, 'User-agent: *')
        self.assertContains(response, 'Allow: /')
        self.assertContains(response, 'Sitemap: https://jdreksler.com/sitemap.xml')

    def test_confirmation_page_is_noindex(self):
        response = self.client.get(reverse('portfolio:thanks'), secure=True)
        self.assertContains(response, '<meta name="robots" content="noindex,follow">')

    def test_images_reserve_layout_space(self):
        projects = self.client.get(reverse('portfolio:projects'), secure=True)
        self.assertContains(projects, 'width="1024" height="576"', count=6)
        resume = self.client.get(reverse('portfolio:resume'), secure=True)
        self.assertContains(resume, 'width="800" height="714"')
