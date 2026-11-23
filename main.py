def analyse_temperature(data: list[float]) -> tuple:

    if not data:
        raise ValueError("Temperature data cannot be empty")

    room_temp = 25.0
    danger_temp = 27.0
    warning_flag = False

    min_valid_temp = 20.0
    max_valid_temp = 25.0

    min_sensor_temp = -40.0
    max_sensor_temp = 80.0

    avg_value = sum(data) / len(data)
    max_value = max(data)
    min_value = min(data)

    max_min = max_value - min_value

    count_above_room = 0
    normal_temp_count = 0

    for temperature in data:
        if temperature > room_temp:
            count_above_room += 1

        if temperature > danger_temp:
            warning_flag = True

        if min_valid_temp <= temperature <= max_valid_temp:
            normal_temp_count += 1

        if not min_sensor_temp <= temperature <= max_sensor_temp:
            print(f"Temperature: {temperature} is not valid, check data")


    if warning_flag:
        print(f"Warning! The temp is above {danger_temp}.")

    percent_above_room = (count_above_room / len(data)) * 100

    print(
        f'average temp: {avg_value}\n'
        f'min temp: {min_value}\n'
        f'max temp: {max_value}\n'
        f'count of temps above room: {count_above_room}\n'
        f'max-min temp: {max_min}\n'
        f'count of temps from 20.0 to 25.0: {normal_temp_count}\n'
        f'above room: {percent_above_room}%\n'
        )
    return avg_value, min_value, max_value, count_above_room, max_min, normal_temp_count, percent_above_room


temperatures = [19.8, 20.1, 21.3, 23.5, 26.2, 28.1, 27.4, 25.9]
invalid_temps = [129.8, 20.1, 21.3, 23.5, 26.2, 28.1, 27.4, 25.9]
empty_temps = []


analyse_temperature(temperatures)