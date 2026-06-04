from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HISTORICAL_CLIENT_DOC_ROOT = Path("docs/contexto rama original/0_desarrollo_del_cliente")
MANDATORY_DOC_ROOT = Path("docs/arquitectura y procedimientos estandar tfg dash")


def read_doc(relative_path):
    return (ROOT / relative_path).read_text(encoding="utf-8")


class Phase1AcceptanceDocsTest(unittest.TestCase):
    def test_acceptance_and_roadmap_docs_exist(self):
        required = [
            HISTORICAL_CLIENT_DOC_ROOT / "phase1_acceptance.md",
            HISTORICAL_CLIENT_DOC_ROOT / "telemetry_column_provenance.md",
            HISTORICAL_CLIENT_DOC_ROOT / "runtime_console_output_contract.md",
            MANDATORY_DOC_ROOT / "arquitectura_y_procedimientos_estandar_tfg_dash.md",
            MANDATORY_DOC_ROOT / "TFG_PLAN_GENERICO.md",
        ]

        for relative_path in required:
            self.assertTrue((ROOT / relative_path).is_file(), relative_path)

    def test_phase1_acceptance_states_required_boundaries(self):
        text = read_doc(HISTORICAL_CLIENT_DOC_ROOT / "phase1_acceptance.md").lower()

        self.assertIn("6f36888", text)
        self.assertIn("13. phase 1 acceptance", text)
        self.assertIn("gstreamer is an integration/demo path", text)
        self.assertIn("not benchmark-grade", text)
        self.assertIn("fakesink", text)
        self.assertIn("faster than real time", text)
        self.assertIn("visible playback", text)
        self.assertIn("not academic benchmark validity", text)
        self.assertIn("fake media engine is the controlled path", text)
        self.assertIn("segment_telemetry.csv", text)
        self.assertIn("evaluation_segments.csv", text)
        self.assertIn("not final benchmark result tables", text)
        self.assertIn("academic abr baselines", text)
        self.assertIn("ai-based abr", text)
        self.assertIn("ppo", text)
        self.assertIn("final qoe metric", text)
        self.assertIn("final reward definition", text)
        self.assertIn("trace infrastructure", text)
        self.assertIn("benchmark scripts", text)
        self.assertIn("gui/operator dashboard", text)
        self.assertIn("return to phase 0 methodology", text)

    def test_phase3_rebuild_context_is_registered_but_bounded(self):
        text = "\n".join(
            [
                read_doc("AGENTS.md").lower(),
                read_doc(MANDATORY_DOC_ROOT / "arquitectura_y_procedimientos_estandar_tfg_dash.md").lower(),
                read_doc(MANDATORY_DOC_ROOT / "TFG_PLAN_GENERICO.md").lower(),
            ]
        )

        self.assertIn("phase 3 rebuild", text)
        self.assertIn("dataset en bruto", text)
        self.assertIn("datasets_normalizados", text)
        self.assertIn("manifests_trazas", text)
        self.assertIn("throughput_kbps", text)
        self.assertIn("no usar dry-runs legacy como training data", text)
        self.assertIn("no producir rankings", text)

    def test_current_docs_do_not_make_legacy_dataset_names_canonical(self):
        current_docs = [
            "README.md",
            "AGENTS.md",
            HISTORICAL_CLIENT_DOC_ROOT / "phase1_acceptance.md",
            HISTORICAL_CLIENT_DOC_ROOT / "output_artifact_contract.md",
        ]

        for relative_path in current_docs:
            text = read_doc(relative_path).lower()
            if "dataset.csv" in text or "dataset_training.csv" in text:
                self.assertIn("deprecated", text, relative_path)
                self.assertNotIn("dataset.csv` is the current canonical", text, relative_path)
                self.assertNotIn("dataset_training.csv` is the current canonical", text, relative_path)


if __name__ == "__main__":
    unittest.main()
