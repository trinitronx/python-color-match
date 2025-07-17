from .util.color import calculate_delta_e


def main():
    print(
        f"This is only printed when running {__file__} directly, because the __name__ is {__name__}"
    )
    print(f"BSD Delta E: {calculate_delta_e('#eb0028', '#d70000')}")


if __name__ == "__main__":
    main()
