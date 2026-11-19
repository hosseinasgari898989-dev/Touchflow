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

path.write_text(source, encoding="utf-8")
print(f"Applied targeted startup fix to {path}")
