Run python fetch_data.py
Traceback (most recent call last):
status: 404
  File "/home/runner/work/congress-trades/congress-trades/fetch_data.py", line 33, in <module>
body (first 200): 404: Not Found
    main()
  File "/home/runner/work/congress-trades/congress-trades/fetch_data.py", line 11, in main
    r.raise_for_status()
  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/requests/models.py", line 1167, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://raw.githubusercontent.com/timothycarambat/house-stock-watcher-data/main/data/all_transactions.json
Error: Process completed with exit code 1.
