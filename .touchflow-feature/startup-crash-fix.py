#!/usr/bin/env python3
import pathlib
import sys

path = pathlib.Path(sys.argv[1])
source = path.read_text(encoding="utf-8")

changes = [
    (
        "        super.onCreate(savedInstanceState)\n"
        "        setNormalSystemBars()\n"
        "        showHome()\n",
        "        super.onCreate(savedInstanceState)\n"
        "        showHome()\n",
        "onCreate startup sequence",
    ),
    (
        "    private fun showHome() {\n"
        "        currentPage = \"home\"\n"
        "        setNormalSystemBars()\n"
        "        val page = pageContainer()\n",
        "    private fun showHome() {\n"
        "        currentPage = \"home\"\n"
        "        val page = pageContainer()\n",
        "showHome pre-content sequence",
    ),
    (
        "        setContentView(scrollable(page))\n"
        "    }\n\n"
        "    private fun showToolsHome()",
        "        setContentView(scrollable(page))\n"
        "        setNormalSystemBars()\n"
        "    }\n\n"
        "    private fun showToolsHome()",
        "post-content system bar sequence",
    ),
    (
        "            saveButton.visibility = if (capturedGroups.isNotEmpty()) View.VISIBLE else View.GONE\n"
        "            stopFloating.visibility = View.GONE\n",
        "            saveButton.visibility = if (capturedGroups.isNotEmpty()) View.VISIBLE else View.GONE\n"
        "            saveButton.isEnabled = capturedGroups.isNotEmpty()\n"
        "            stopFloating.visibility = View.GONE\n",
        "enable save only after a non-empty recording",
    ),
]

for old, new, label in changes:
    count = source.count(old)
    if count != 1:
        raise SystemExit(f"Expected exactly one match for {label}; found {count}")
    source = source.replace(old, new, 1)

on_create = source.split("override fun onCreate", 1)[1].split("private fun handleWidgetHelpIntent", 1)[0]
home = source.split("private fun showHome()", 1)[1].split("private fun showToolsHome()", 1)[0]
if "setNormalSystemBars()" in on_create:
    raise SystemExit("onCreate still calls setNormalSystemBars()")
if home.index("setNormalSystemBars()") < home.index("setContentView(scrollable(page))"):
    raise SystemExit("showHome calls setNormalSystemBars() before setContentView")

stopped_controls = source.split("fun showStoppedControls(message: String) {", 1)[1].split("\n        }", 1)[0]
visibility_line = "saveButton.visibility = if (capturedGroups.isNotEmpty()) View.VISIBLE else View.GONE"
enabled_line = "saveButton.isEnabled = capturedGroups.isNotEmpty()"
if visibility_line not in stopped_controls or enabled_line not in stopped_controls:
    raise SystemExit("save button state is not derived from captured groups")
if stopped_controls.index(visibility_line) > stopped_controls.index(enabled_line):
    raise SystemExit("save button enabled-state update order is invalid")

path.write_text(source, encoding="utf-8")
print(f"Applied startup and save-enable fixes to {path}")
