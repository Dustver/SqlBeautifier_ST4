import os
import sys
from typing import Optional

import sublime
import sublime_plugin

sys.path.append(os.path.dirname(__file__))

import sqlparse


settings: Optional[sublime.Settings] = None


def plugin_loaded() -> None:
    global settings
    settings = sublime.load_settings("SQL Beautifier.sublime-settings")


class SqlBeautifierCommand(sublime_plugin.TextCommand):
    def format_sql(self, raw_sql: str) -> Optional[str]:
        if settings is None:
            return None

        try:
            formatted_sql = sqlparse.format(
                raw_sql,
                keyword_case=settings.get("keyword_case"),
                identifier_case=settings.get("identifier_case"),
                strip_comments=settings.get("strip_comments"),
                indent_tabs=settings.get("indent_tabs"),
                indent_width=settings.get("indent_width"),
                reindent=settings.get("reindent"),
            )

            if self.view.settings().get("ensure_newline_at_eof_on_save"):
                formatted_sql += "\n"

            return formatted_sql
        except Exception as e:
            print(f"SqlBeautifier error: {e}")
            return None

    def replace_region_with_formatted_sql(
        self, edit: sublime.Edit, region: sublime.Region
    ) -> None:
        selected_text = self.view.substr(region)
        formatted_text = self.format_sql(selected_text)
        if formatted_text is not None:
            self.view.replace(edit, region, formatted_text)

    def run(self, edit: sublime.Edit) -> None:
        for region in self.view.sel():
            if region.empty():
                selection = sublime.Region(0, self.view.size())
                self.replace_region_with_formatted_sql(edit, selection)
                # Ensure syntax file is set to ST4/ST3 specific syntax path
                self.view.assign_syntax("Packages/SQL/SQL.sublime-syntax")
            else:
                self.replace_region_with_formatted_sql(edit, region)
