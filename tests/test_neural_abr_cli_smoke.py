from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class NeuralAbrCliSmokeTest(unittest.TestCase):
    def test_phase4d_cli_synthetic_smoke(self):
        repo_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir = root / "dataset"
            run_dir = root / "run"
            validation_dir = root / "validation"

            commands = (
                [sys.executable, "scripts/build_neural_abr_dataset.py", "--synthetic-smoke", "--output-dir", str(dataset_dir), "--overwrite"],
                [sys.executable, "scripts/validate_neural_abr_dataset.py", "--dataset-dir", str(dataset_dir)],
                [
                    sys.executable,
                    "scripts/train_neural_abr.py",
                    "--dataset-dir",
                    str(dataset_dir),
                    "--output-dir",
                    str(run_dir),
                    "--epochs",
                    "1",
                    "--batch-size",
                    "8",
                    "--seed",
                    "123",
                    "--device",
                    "cpu",
                    "--smoke",
                ],
                [
                    sys.executable,
                    "scripts/validate_neural_abr_offline.py",
                    "--dataset-dir",
                    str(dataset_dir),
                    "--run-dir",
                    str(run_dir),
                    "--output-dir",
                    str(validation_dir),
                ],
            )
            for command in commands:
                with self.subTest(command=command[1]):
                    completed = subprocess.run(command, cwd=repo_root, text=True, capture_output=True, check=False)
                    self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)

            self.assertTrue((dataset_dir / "dataset_validation_report.json").is_file())
            self.assertTrue((run_dir / "training_report.json").is_file())
            self.assertTrue((validation_dir / "offline_validation_report.json").is_file())


if __name__ == "__main__":
    unittest.main()
