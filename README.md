SqlBeautifier
============================

This is a SQL formatter plugin for **Sublime Text 4** using [python-sqlparse](https://github.com/andialbrecht/sqlparse).

*Note: This is a highly optimized fork specifically aimed at modernizing the codebase for Sublime Text 4, utilizing Python 3.8 and removing legacy support for older Sublime Text versions.*

Enjoy!

### Installation
Please install Sublime [Package Control](https://packagecontrol.io/installation) first. Then inside *Package Control: Install Package*, type *SqlBeautifier* and then click to confirm.


### Settings
#### The default key binding for Mac is 

```json
{ "keys": ["super+k", "super+f"], "command": "sql_beautifier" }
```

* Kindly note that the `super` key here is generally replaced by the `Command (⌘)` key.

#### The default key binding for Windows / Linux is

```json
{ "keys": ["ctrl+k", "ctrl+f"], "command": "sql_beautifier" }
```

#### Options for formatter

To change the options, click through *Preferences -> Package Settings -> Sql Beautifier -> Settings - User* and add the overridden options in JSON like this:

```json
{
	"indent_tabs": true,
	"indent_width": 1
}
```

This overrides the default options at *Preferences -> Package Settings -> Sql Beautifier -> Settings - Default*.

Here is the list of options the formatter supports:

- **keyword_case**: Changes how keywords are formatted. Allowed values are `"upper"`, `"lower"` and `"capitalize"` and `null` (leaves case intact).

- **identifier_case**: Changes how identifiers are formatted. Allowed values are `"upper"`, `"lower"`, and `"capitalize"` and `null` (leaves case intact).

- **strip_comments**: If `true` comments are removed from the statements.

- **reindent**: If `true` the indentations of the statements are changed.

- **indent_tabs**: If `true` tabs instead of spaces are used for indentation.

- **indent_width**: The width of the indentation, defaults to 2.
