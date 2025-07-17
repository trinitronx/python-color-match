#!/usr/bin/env python

print(f"This is printed because {__file__} was included")

if __name__ == '__main__':
    print(f"This is only printed when running {__file__} directly, because the __name__ is {__name__}")
    print(f"BSD Delta E: {calculate_delta_e("#eb0028", "#d70000")}")
