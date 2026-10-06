# Objectives

| ID | Field | Entry |
|---|---|---|
| MO-1 | What is measured | API response time for annotation counts per class |
| | How | Browser Network panel, Timing tab, GET request duration |
| | Target | Median of 5 runs at or below 400ms |
| | Conditions | Chrome, cache disabled, local Docker, COCO val2017 loaded |

## Results
- Run 1: 377 ms
- Run 2: 353 ms
- Run 3: 349 ms
- Run 4: 274 ms
- Run 5: 352 ms
- Median: 352 ms ✅ (target was ≤ 400 ms)
- Spread: 274 ms – 377 ms (range 103 ms, all warm runs)

## Environment
- CPU: Intel Core i5-6300U @ 2.40GHz (4 CPUs)
- RAM: 8 GB (8192 MB)
- OS: Windows 10 Pro 64-bit (Build 19045)
- CVAT SHA: c4f0c2a54dd7d95bc222836c645e8c290858fd05