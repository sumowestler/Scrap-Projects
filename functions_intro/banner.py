def banner_text(text=" ", screen_width=80):

    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than the specified width {1}".format(text, screen_width))
        # Raise is used to raise an exemption in your code.
        # print("EEK!!", 60)
        # print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH", 60)

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = "**{}**".format(centered_text)
        print(output_string)


banner_text("*", 60)
banner_text("Always look on the bright side of life", 60)
banner_text("If life seems jolly rotten", 60)
banner_text(screen_width=60)
banner_text("Theres something you've forgotten!", 60)
banner_text("55555555555555555555555555555555555555555555555555555555555", 66)
