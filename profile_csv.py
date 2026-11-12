import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()
# Call your plain-Python CSV processing function here.
profiler.disable()
pstats.Stats(profiler).sort_stats("cumulative").print_stats(15)
