import hashlib
import json
import tempfile
import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import qiita_gateway as qg


class QiitaGatewayTests(unittest.TestCase):
    def make_repo(self, action="publish_new", item_id=""):
        td = tempfile.TemporaryDirectory()
        root = Path(td.name)
        (root / "public").mkdir()
        (root / ".qiita-gateway/requests").mkdir(parents=True)
        body = "## 本文\n\nテストです。\n"
        front = "---\ntitle: テスト記事\ntags:\n  - AI\n  - Security\nprivate: false\nupdated_at: \"\"\nid: \"%s\"\norganization_url_name: null\nslide: false\nignorePublish: false\n---\n" % item_id
        article = front + body
        ap = root / "public/test.md"
        ap.write_text(article, encoding="utf-8")
        rendered_sha = hashlib.sha256(ap.read_bytes()).hexdigest()
        body_sha = hashlib.sha256(body.encode()).hexdigest()
        request_id = "11111111-1111-1111-1111-111111111111"
        req = {
            "schema": qg.REQUEST_SCHEMA,
            "request_id": request_id,
            "issued_at": "2026-08-14T22:00:00+09:00",
            "action": action,
            "article": {
                "path": "public/test.md",
                "source_body_sha256": body_sha,
                "rendered_file_sha256": rendered_sha,
                "title": "テスト記事",
                "tags": ["AI", "Security"],
            },
            "existing_article": None if action == "publish_new" else {
                "repository_path": "public/test.md",
                "qiita_item_id": item_id,
            },
            "approval": {
                "actor_type": "human",
                "actor_id": "director",
                "approved_at": "2026-08-14T22:01:00+09:00",
                "approved_rendered_file_sha256": rendered_sha,
            },
            "deployment": {
                "repository": "umayado17/zenn-content",
                "branch": "main",
                "workflow": ".github/workflows/publish.yml",
            },
        }
        rp = root / ".qiita-gateway/requests" / f"{request_id}.json"
        rp.write_text(json.dumps(req, ensure_ascii=False, indent=2), encoding="utf-8")
        return td, root, rp, req, body

    def test_valid_new_request(self):
        td, root, rp, req, body = self.make_repo()
        try:
            changed = ["public/test.md", rp.relative_to(root).as_posix()]
            info = qg.validate_request(rp, root, changed)
            self.assertEqual(info["action"], "publish_new")
        finally:
            td.cleanup()

    def test_reject_hash_mismatch(self):
        td, root, rp, req, body = self.make_repo()
        try:
            p = root / "public/test.md"
            p.write_text(p.read_text(encoding="utf-8") + "改変\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                qg.validate_request(rp, root, None)
        finally:
            td.cleanup()

    def test_reject_ambiguous_changes(self):
        td, root, rp, req, body = self.make_repo()
        try:
            (root / "public/other.md").write_text("x", encoding="utf-8")
            with self.assertRaises(ValueError):
                qg.validate_request(rp, root, ["public/test.md", "public/other.md", rp.relative_to(root).as_posix()])
        finally:
            td.cleanup()

    def test_valid_update_identity(self):
        td, root, rp, req, body = self.make_repo(action="update_existing", item_id="abc123")
        try:
            info = qg.validate_request(rp, root, None)
            self.assertEqual(info["existing_qiita_item_id"], "abc123")
        finally:
            td.cleanup()

    def test_remote_exact_match_is_published(self):
        td, root, rp, req, body = self.make_repo(action="update_existing", item_id="abc123")
        try:
            info = qg.validate_request(rp, root, None)
            remote = {"id": "abc123", "url": "https://qiita.com/example/items/abc123", "title": "テスト記事", "body": body}
            status, error = qg.evaluate_remote(info, remote, "abc123", 0)
            self.assertEqual(status, "PUBLISHED")
            self.assertIsNone(error)
        finally:
            td.cleanup()

    def test_select_exact_remote(self):
        td, root, rp, req, body = self.make_repo()
        try:
            info = qg.validate_request(rp, root, None)
            items = [
                {"id": "x", "url": "https://qiita.com/example/items/x", "title": "別記事", "body": body},
                {"id": "abc", "url": "https://qiita.com/example/items/abc", "title": "テスト記事", "body": body},
            ]
            selected = qg.select_exact_remote(info, items)
            self.assertEqual(selected["id"], "abc")
        finally:
            td.cleanup()

    def test_bind_frontmatter_item_id(self):
        td, root, rp, req, body = self.make_repo()
        try:
            article = root / "public/test.md"
            qg.bind_frontmatter_item_id(article, "abc123")
            front, _ = qg.split_front_matter(article.read_text(encoding="utf-8"))
            self.assertEqual(qg.parse_simple_front_matter(front)["id"], "abc123")
            with self.assertRaises(ValueError):
                qg.bind_frontmatter_item_id(article, "different")
        finally:
            td.cleanup()

    def test_cli_failure_without_remote_is_unknown(self):
        td, root, rp, req, body = self.make_repo()
        try:
            info = qg.validate_request(rp, root, None)
            status, error = qg.evaluate_remote(info, None, None, 1)
            self.assertEqual(status, "UNKNOWN")
            self.assertEqual(error["code"], "PUBLISH_SIDE_EFFECT_UNKNOWN")
        finally:
            td.cleanup()


if __name__ == "__main__":
    unittest.main()
