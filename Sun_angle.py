def sun_angle(time):
    delta = 90 / 6
    delta_second = delta / 60
    hours, minute = time.split(":")
    # print(int(hours), int(minute))
    hours = int(hours)
    minute = int(minute)
    if (hours == 6 or hours == 18) and minute > 0:
        return "I don't see the sun!"
    if hours >= 6 and hours <= 18:
        return (hours - 6) * delta + delta_second * minute
    return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    assert sun_angle("07:00") == 15
    assert sun_angle("18:00") == 180
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")

print(sun_angle("12:15"))