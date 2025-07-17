
def main():
    print(
        f"This is only printed when running {__file__} directly, because the __name__ is {__name__}"
    )


if __name__ == "__main__":
    main()
