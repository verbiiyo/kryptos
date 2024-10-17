from crack import plot_char_frequencies, get_char_frequencies, get_char_frequencies, k4_no_spaces


random_english_text = """

Why Countries Use Different Timezones: A Global Necessity

The concept of time has always been central to human civilization, dictating the rhythm of daily life, economic activity, and international relations. With the advancement of global travel, trade, and communication, the need for a standardized system to organize time became paramount. Time zones were established as a solution, enabling the coordination of activities across different regions of the world. But why do countries use different time zones, and what are the benefits of this system? This essay explores the reasons why countries adopt different time zones, focusing on geography, societal needs, and international synchronization.

Geography and Earth's Rotation
The most fundamental reason for the existence of time zones is geography. The Earth is a rotating sphere, and as it spins on its axis, different parts of the world experience daylight and darkness at different times. If the entire world operated on the same time, some places would find themselves experiencing midnight at noon, making it impossible to structure daily activities around natural light. Therefore, time zones are necessary to align the hours of the day with the position of the sun.

The Earth is divided into 24 time zones, each covering 15 degrees of longitude. This division ensures that, as the Earth rotates, each region experiences daylight and nighttime in a manner consistent with the sun’s movement. By dividing the world into time zones, countries can maintain a logical structure where the local time corresponds to the actual position of the sun in the sky.

Societal and Economic Efficiency
Countries also adopt different time zones to optimize societal and economic efficiency. Different regions may have specific needs based on their geographic location, population density, and economic activity. For example, a large country like Russia, which spans 11 time zones, ensures that local time aligns with the natural daylight hours across its vast territory. This allows people to work, attend school, and conduct business during daylight hours, improving productivity and the well-being of its population.

In contrast, smaller countries or countries located within a single longitudinal range may adopt one time zone to simplify governance and economic activities. China, despite its vast size, operates under a single time zone (China Standard Time, UTC+8) for political and administrative uniformity, even though this leads to some regions experiencing daylight much earlier or later than others.

International Coordination and Standardization
The adoption of time zones also facilitates international coordination. In a globalized world, where trade, travel, and communication occur across national borders, time zones help standardize when activities can happen in different countries. For instance, businesses that operate internationally need to know what time it is in other parts of the world to schedule meetings, trade goods, or engage with partners.

The International Meridian Conference of 1884 established the Greenwich Meridian (now called the Prime Meridian) as the global reference point for time zones, with Coordinated Universal Time (UTC) as the standard. This system allows countries to base their local times on UTC, ensuring a standardized reference for global coordination.

Time zones also impact international transportation and communication systems. Airlines, for example, base their schedules on time zone differences to organize flights, while telecommunications and satellite systems rely on accurate time synchronization across different zones. This global framework is essential for keeping the world connected.

Daylight Saving Time and Local Adjustments
In addition to standard time zones, some countries use daylight saving time (DST) to make better use of daylight during certain periods of the year. By adjusting the clocks forward by an hour in the summer months, countries can extend evening daylight, reducing the need for artificial lighting and aligning working hours with the natural daylight cycle. Countries in higher latitudes, such as the United States, parts of Europe, and Australia, often implement DST to take advantage of longer daylight hours in the summer. However, this practice is not universal, with many countries near the equator—where daylight variation is minimal—opting not to adopt DST.

Political and Cultural Considerations
In some cases, time zones are shaped by political and cultural factors rather than purely geographic ones. National pride, economic ties, or historical connections can lead a country to align its time zone with a specific region. For example, Spain, although geographically located in the same zone as the UK (UTC+0), aligns its time with Central European Time (UTC+1) due to historical ties and economic connections with its European neighbors.

Similarly, some countries use multiple time zones to reflect regional autonomy or cultural diversity. India, despite its vast size, uses one time zone, while other large countries like the United States or Russia have several, reflecting the differing regional needs across vast territories.

Conclusion
Countries use different time zones primarily to align daily activities with the Earth's rotation, maximizing the use of daylight for societal, economic, and environmental benefits. These time zones facilitate global coordination, ensuring that international trade, communication, and travel can occur efficiently across the world. Adjustments such as daylight saving time and the influence of political decisions further shape time zone usage, reflecting the complex ways in which human societies adapt to the movement of the Earth and the demands of modern life. Time zones, while seemingly simple, are essential to the smooth functioning of a globalized world.

"""

plot_char_frequencies(random_english_text)


char_counts, sorted_chars = get_char_frequencies(random_english_text)

def frequency_decrypt(text: str):
    # basically, let's decrypt by matching up the frequency sorts as our key
    # and then just replace the characters
    input_char_counts, input_sorted_chars = get_char_frequencies(text)

    # the key is from the input sorted chars to the sorted chars
    key = {input_char: char for input_char, char in zip(input_sorted_chars, sorted_chars)}

    # decrypt the text
    decrypted_text = "".join([key.get(char, char) for char in text])
    return decrypted_text

print(frequency_decrypt(k4_no_spaces))

