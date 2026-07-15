from pathlib import Path
import sys
import tempfile
import unittest
import zipfile


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from build_skill_package import SKILL_NAME, build_package  # noqa: E402


class BuildSkillPackageTests(unittest.TestCase):
    def test_package_is_minimal_installable_and_reproducible(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first.zip"
            second = Path(directory) / "second.zip"
            _, first_digest, first_count = build_package(first)
            _, second_digest, second_count = build_package(second)

            self.assertEqual(first_digest, second_digest)
            self.assertEqual(first_count, second_count)
            with zipfile.ZipFile(first) as archive:
                names = set(archive.namelist())

            prefix = f"{SKILL_NAME}/"
            self.assertIn(prefix + "SKILL.md", names)
            self.assertIn(prefix + "agents/openai.yaml", names)
            self.assertIn(prefix + "scripts/seedance_client.py", names)
            self.assertIn(prefix + "templates/single-15s.md", names)
            self.assertIn(prefix + "templates/revision-preview.md", names)
            self.assertIn(prefix + "references/runtime-orchestration.md", names)
            self.assertIn(prefix + "references/targeted-regeneration.md", names)
            self.assertIn(prefix + ".env.example", names)
            self.assertNotIn(prefix + ".env", names)
            self.assertNotIn(prefix + "README.md", names)
            self.assertFalse(any(name.startswith(prefix + "docs/") for name in names))
            self.assertFalse(any(name.startswith(prefix + "tests/") for name in names))
            self.assertFalse(any(name.startswith(prefix + "assets/") for name in names))


if __name__ == "__main__":
    unittest.main()
