# Objectives

| ID | Field | Entry |
|---|---|---|
| MO-1 | What is measured | API response time for annotation counts per class |
| | How | Browser Network panel, Timing tab, GET request duration |
| | Target | Median of 5 runs at or below 400ms |
| | Conditions | Chrome, cache disabled, local Docker, COCO val2017 loaded |

## Results
- Run 1: 708 ms (cold start)
- Run 2: 377 ms
- Run 3: 349 ms
- Run 4: 274 ms
- Run 5: 353 ms
- Median: 353 ms ✅ (target was ≤ 400 ms)
- Spread: 274 ms – 708 ms (range 434 ms; Run 1 is cold-start outlier; warm median 349 ms)

## Environment
- CPU: Intel Core i5-6300U @ 2.40GHz (4 CPUs)
- RAM: 8 GB (8192 MB)
- OS: Windows 10 Pro 64-bit (Build 19045)
- CVAT SHA: c4f0c2a54dd7d95bc222836c645e8c290858fd05