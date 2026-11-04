
import time
import statistics
import urllib.request
import sys

URL = "https://studenthub-staging.onrender.com"
TOTAL_REQUESTS = 10

def measure_request():
    request = urllib.request.Request(
        URL,
        headers={"User-Agent": "StudentHub-Performance-Test"}
    )

    start = time.perf_counter()

    with urllib.request.urlopen(request, timeout=120) as response:
        status = response.status
        response.read()

    elapsed = (time.perf_counter() - start) * 1000
    return elapsed, status


print("=" * 55)
print("STUDENTHUB STAGING PERFORMANCE TEST")
print("=" * 55)
print("URL:", URL)

try:
    print("\nTesting first request...")
    cold_time, status = measure_request()

    print(f"First response: {cold_time:.2f} ms")
    print("HTTP Status:", status)

    timings = []

    print("\nTesting subsequent requests...")

    for number in range(1, TOTAL_REQUESTS + 1):
        elapsed, status = measure_request()
        timings.append(elapsed)
        print(f"Request {number}: {elapsed:.2f} ms")

    ordered = sorted(timings)
    p95 = ordered[int(0.95 * (len(ordered) - 1))]

    print("\n" + "=" * 55)
    print("PERFORMANCE TEST RESULTS")
    print("=" * 55)
    print("Total requests:", TOTAL_REQUESTS)
    print(f"Average: {statistics.mean(timings):.2f} ms")
    print(f"Median: {statistics.median(timings):.2f} ms")
    print(f"Approx. P95: {p95:.2f} ms")
    print(f"Minimum: {min(timings):.2f} ms")
    print(f"Maximum: {max(timings):.2f} ms")
    print("HTTP Status:", status)
    print("=" * 55)

except Exception as error:
    print("\nPERFORMANCE TEST FAILED")
    print("Error:", error)
    sys.exit(1)
