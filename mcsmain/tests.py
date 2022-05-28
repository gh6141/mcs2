from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from django.urls import resolve

from mcsmain.models import Mcsmain
from mcsmain.views import top, mcsmain_new, mcsmain_edit, mcsmain_detail

UserModel = get_user_model()


class TopPageTest(TestCase):
    def test_top_page_returns_200_and_expected_title(self):
        response = self.client.get("/")
        self.assertContains(response, "Blanche", status_code=200)

    def test_top_page_uses_expected_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "mcsmain/top.html")


class TopPageRenderSnippetsTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="top_secret_pass0001",
        )
        self.mcsmain = Mcsmain.objects.create(
            title="title1",
            naiyo="print('hello')",
            hitokoto="description1",
            created_by=self.user,
        )

    def test_should_return_snippet_title(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.mcsmain.title)

    def test_should_return_username(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.user.username)



class SnippetDetailTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="secret",
        )
        self.mcsmain = Mcsmain.objects.create(
            title="タイトル",
            naiyo="コード",
            hitokoto="解説",
            created_by=self.user,
        )

    def test_should_use_expected_template(self):
        response = self.client.get("/mcsmain/%s/" % self.mcsmain.id)
        self.assertTemplateUsed(response, "mcsmain/mcsmain_detail.html")

    def test_top_page_returns_200_and_expected_heading(self):
        response = self.client.get("/mcsmain/%s/" % self.mcsmain.id)
        self.assertContains(response, self.mcsmain.title, status_code=200)
