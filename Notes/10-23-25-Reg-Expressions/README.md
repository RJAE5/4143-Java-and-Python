## Java and Python Notes
### 10-23-2025 Python Regular Expressions

#### Quick Guide
`^` -> Matches the beginning of a line
`$` -> Matches the end of the line
`.` -> Matches any one character except newline; with DOTALL, includes new line character
`\s` -> Matches white space
`\S` -> Matches any non-whitespace character
`*` -> Repeats a character zero or more times
`?` -> Repeats a character zero or one times
`*?` -> (non-greedy)
`+` -> Repeats a character one or more times
`+?` -> (Non-greedy)

#### Using RegEx
You must `import re`, and you can use `re.search()` to see if a string matches a regular expression. You can also use `re.findall()` to extract portions of a string that match your regular expression.

#### Wild Card Characters
The dot character maches any character (except newline)

`F..m:` matches `From:`, `Fxxm:`, `F12m:` and literally everything else just not counting a newline.

#### Helpful tools
regex101.com is helpful for explaining and demonstrating regular expressions.