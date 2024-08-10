async def formatter(lessons_data):
    temp = []

    for i in range(len(lessons_data)):
        temp.append((i, lessons_data[i]))

    result = '\n\n'.join(f'{item[0]} --- {item[2]} --- {item[1]}' for item in temp)
    return result
