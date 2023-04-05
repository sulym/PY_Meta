report_file = {
    "./test_source_code_2.py": [],
    "./source_code_2.py":
        [
            {
                "code": "E501",
                "filename": "./source_code_2.py",
                "line_number": 18,
                "column_number": 80,
                "text": "line too long (99 > 79 characters)",
                "physical_line": '    return f"I like to filter, rounding, doubling, '
                "store and decorate numbers: {', '.join(items)}!\"",
            },
            {
                "code": "W292",
                "filename": "./source_code_2.py",
                "line_number": 18,
                "column_number": 100,
                "text": "no newline at end of file",
                "physical_line": '    return f"I like to filter, rounding, doubling, '
                "store and decorate numbers: {', '.join(items)}!\"",
            },
        ]
}

def format_linter_error(error: dict) -> dict:
    # write your code here
    return {
            "line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"
            }

def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    return {
            "errors": [format_linter_error(one_eror) for one_eror in errors],
            "path": file_path,
            "status": "failed" if errors else "passed"
            }


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    return [format_single_linter_file(path, err) for path, err in linter_report.items()]


print(format_linter_report(linter_report=report_file))


"""# The output will be:

https://github.com/sulym/py-linter-formatter

[
    {
        "errors": [], 
        "path": "./test_source_code_2.py", 
        "status": "passed"
    }, 
    {
        "errors": 
            [
                {
                    "line": 18, 
                    "column": 80, 
                    "message": "line too long (99 > 79 characters)", 
                    "name": "E501", 
                    "source": "flake8"
                }, 
                {
                    "line": 18, 
                    "column": 100, 
                    "message": "no newline at end of file", 
                    "name": "W292", 
                    "source": "flake8"
                }
            ], 
        "path": "./source_code_2.py", 
        "status": "failed"
    }
]
"""