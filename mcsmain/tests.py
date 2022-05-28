from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from mcsmain.views import top,mcsmain_new,mcsmain_edit,mcsmain_detail


class TopPageViewTest(TestCase):
    def test_top_returns_200(self):
        request = HttpRequest()  # HttpRequestオブジェクトの作成
        response = top(request)
        self.assertEqual(response.status_code, 200)

    def test_top_returns_expected_content(self):
        request = HttpRequest()  # HttpRequestオブジェクトの作成
        response = top(request)
        self.assertEqual(response.content, b"Test Test")

class TopPageTest(TestCase):
    def test_top_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_top_returns_expected_content(self):
        response = self.client.get("/")
        self.assertEqual(response.content, b"Test Test")


class CreateMcsmainTest(TestCase):
    def test_should_resolve_mcsmain_new(self):
        found = resolve("/mcsmain/new/")
        self.assertEqual(mcsmain_new, found.func)


class McsmainDetailTest(TestCase):
    def test_should_resolve_mcsmain_detail(self):
        found = resolve("/mcsmain/1/")
        self.assertEqual(mcsmain_detail, found.func)


class EditMcsmainTest(TestCase):
    def test_should_resolve_mcsmain_edit(self):
        found = resolve("/mcsmain/1/edit/")
        self.assertEqual(mcsmain_edit, found.func)


