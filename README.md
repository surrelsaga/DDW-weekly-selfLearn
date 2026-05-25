# Lessons

## Week 02 — Heapsort

### Attempt 1
Got `heapSort` working, but to restrict `build_max_heap` to only the active (unsorted) portion of the array, I had to add an extra `heap_end_pos` argument to `build_max_heap` and replace `len(arr)` with it wherever the boundary was used. It worked, but it changed the function signature just to support a heapsort use case.

### Attempt 2 — Refactor using list slicing
*(commit `60ee5ec`)*

Instead of telling `build_max_heap` where to stop, I just give it the exact portion of the array it needs to work on using Python list slicing. The steps are:
1. Slice the active heap portion out of the array.
2. Run `build_max_heap` on that slice.
3. Write the result back into the original array at the same range.

This keeps `build_max_heap` simple (no extra parameter) and makes the intent at the call site clearer. The trade-off is that slicing creates a temporary copy each iteration, but for the purposes of this learning exercise it is a clean and readable approach.

**Key reminder:** Python list slicing returns a *copy*, not a view — always reassign back to the original array if you want changes to persist. Thanks to python revision in week 02, it reminds me of python list slicing.
