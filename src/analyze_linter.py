from pylint.reporters import JSONReporter
from pylint import lint
from glob import glob
from io import StringIO
import pandas as pd
import json
import os


def pylint_project(path):
    pylint_options = ["--recursive=True","--disable=F0010"]
    reporter_buffer = StringIO()
    filepath=os.path.abspath(path)
    results = lint.Run( pylint_options+[filepath] , reporter=JSONReporter(reporter_buffer), exit=False)
    file_results = json.loads(reporter_buffer.getvalue())
    reporter_buffer.close()
    global_score=results.linter.stats.global_note
    print(global_score)
    print(json.dumps(file_results,indent=4))

if __name__ == "__main__":
    try:
        overview, results = pylint_project("/mnt/c/home/pyanalyze_dev/pyanalyze/tests/sample1")
    except Exception as e:
        print(f"An error occurred: {e}")

# from pylint.reporters import JSONReporter
# from pylint.lint import Run
# from glob import glob
# from io import StringIO
# import json
# import os


# def pylint_project(path):
#     pylint_options = ["--disable=F0010"]
#     pylint_overview = []
#     pylint_results = []
#     glob_pattern = os.path.join(path, "**", "*.py")
#     for filepath in glob(glob_pattern, recursive=True):
#         reporter_buffer = StringIO()
#         results = Run([filepath] + pylint_options, reporter=JSONReporter(reporter_buffer))
#         score = results.linter.stats.global_note
#         file_results = json.loads(reporter_buffer.getvalue())
#         pylint_results.extend(file_results)
#         pylint_overview.append({
#             "filepath": os.path.realpath(filepath),
#             "smell_count": len(file_results),
#             "score": score
#         })
#         reporter_buffer.close()
#     return pylint_overview, pylint_results

# if __name__ == "__main__":
#     overview, results = pylint_project("/mnt/c/home/pyanalyze_dev/pyanalyze/tests/sample1/")
#     print("### Overview")
#     print(overview)
#     print("\n### All Results")
#     print(results)