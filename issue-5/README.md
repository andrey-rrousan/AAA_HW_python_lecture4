## ISSUE-5 TEST README
To test the what_is_year_now function you should type the following command in terminal:
"""bash
python -m pytest -v what_is_year_now.py
"""

To get a closer look at test coverage you should type:

"""bash
python -m pytest -q what_is_year_now.py --cov
"""

To get the detailed info at coverage line by line you can generate html file using the following command:

"""bash
python -m pytest -q what_is_year_now.py --cov . --cov-report html
"""

Pretested results are stored in result.txt and in htmlcov folder.