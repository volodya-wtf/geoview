from django.http import response
from map.models import Customer, Unit
from django.shortcuts import render
import folium
from django.http import HttpResponse

# Выбор по МО
def municipal_all(request, municipalDistrict):
    units = Unit.objects.filter(municipalDistrict=municipalDistrict)

    figure = folium.Figure()
    map = folium.Map(location=[53.761683, 87.125225], zoom_start=8)
    map.add_to(figure)

    for unit in units:
        # Unit marker add to map
        folium.CircleMarker(
            location=[unit.lat, unit.lon],
            radius=10,
            popup="#" + str(unit.n_mt),
            color="#097969",
            fill=True,
            fill_color="#3186cc",
        ).add_to(map)

        customers = Customer.objects.filter(unit=unit)
        # Customer marker's and path add to map
        for customer in customers:
            folium.CircleMarker(
                location=[customer.lat, customer.lon],
                radius=10,
                popup=customer.street + ", " + str(customer.building),
                color="#FF5733",
                fill=True,
                fill_color="#3186cc",
            ).add_to(map)
            # Draw path
            folium.PolyLine(
                [[customer.lat, customer.lon], [unit.lat, unit.lon]]
            ).add_to(map)

    figure.render()

    context = {"map": figure, "geodata": municipalDistrict}
    return render(request, "map/map.html", context)

# Выбор по городу
def city_all(request, city):
    units = Unit.objects.filter(city=city)

    figure = folium.Figure()
    map = folium.Map(location=[53.761683, 87.125225], zoom_start=8)
    map.add_to(figure)

    for unit in units:
        # Unit marker add to map
        folium.CircleMarker(
            location=[unit.lat, unit.lon],
            radius=10,
            popup="#" + str(unit.n_mt),
            color="#097969",
            fill=True,
            fill_color="#3186cc",
        ).add_to(map)

        customers = Customer.objects.filter(unit=unit)
        # Customer marker's and path add to map
        for customer in customers:
            folium.CircleMarker(
                location=[customer.lat, customer.lon],
                radius=10,
                popup=customer.street + ", " + str(customer.building),
                color="#FF5733",
                fill=True,
                fill_color="#3186cc",
            ).add_to(map)
            # Draw path
            folium.PolyLine(
                [[customer.lat, customer.lon], [unit.lat, unit.lon]]
            ).add_to(map)

    figure.render()

    context = {"map": figure, "geodata": city}
    return render(request, "map/map.html", context)

# Выбор по району
def district_all(request, cityDistrict):
    units = Unit.objects.filter(cityDistrict=cityDistrict)

    figure = folium.Figure()
    map = folium.Map(location=[53.761683, 87.125225], zoom_start=8)
    map.add_to(figure)

    for unit in units:
        # Unit marker add to map
        folium.CircleMarker(
            location=[unit.lat, unit.lon],
            radius=10,
            popup="#" + str(unit.n_mt),
            color="#097969",
            fill=True,
            fill_color="#3186cc",
        ).add_to(map)

        customers = Customer.objects.filter(unit=unit)
        # Customer marker's and path add to map
        for customer in customers:
            folium.CircleMarker(
                location=[customer.lat, customer.lon],
                radius=10,
                popup=customer.street + ", " + str(customer.building),
                color="#FF5733",
                fill=True,
                fill_color="#3186cc",
            ).add_to(map)
            # Draw path
            folium.PolyLine(
                [[customer.lat, customer.lon], [unit.lat, unit.lon]]
            ).add_to(map)

    figure.render()

    context = {"map": figure, "geodata": cityDistrict}
    return render(request, "map/map.html", context)

# Выбор объекта по номеру в МТ
def unit(request, n_mt):
    val = request.GET.get("q")
    if val:
        try:
            # If unit not exists
            exists = Unit.objects.filter(n_mt=val)
            if not exists:
                return render(request, "map/unit_not_exists.html")
        except:
            return render(request, "map/unit_not_exists.html")

        figure = folium.Figure()
        unit = Unit.objects.get(n_mt=val)
        customers = Customer.objects.filter(unit=unit)

        map = folium.Map(location=[unit.lat, unit.lon], zoom_start=13)
        map.add_to(figure)

        # Unit marker add to map
        folium.CircleMarker(
            location=[unit.lat, unit.lon],
            radius=10,
            popup="#" + str(unit.n_mt),
            color="#097969",
            fill=True,
            fill_color="#3186cc",
        ).add_to(map)

        # Customer marker's and path add to map
        for customer in customers:
            folium.CircleMarker(
                location=[customer.lat, customer.lon],
                radius=10,
                popup=customer.street + ", " + str(customer.building),
                color="#FF5733",
                fill=True,
                fill_color="#3186cc",
            ).add_to(map)
            # Draw path
            folium.PolyLine(
                [[customer.lat, customer.lon], [unit.lat, unit.lon]]
            ).add_to(map)

        figure.render()

        context = {"map": figure, "address": str(unit.address), "n_mt": unit.n_mt}
        return render(request, "map/unit.html", context)

    # If unit not exists
    exists = Unit.objects.filter(n_mt=n_mt)
    if not exists:
        return render(request, "map/unit_not_exists.html")

    figure = folium.Figure()
    unit = Unit.objects.get(n_mt=n_mt)
    customers = Customer.objects.filter(unit=unit)

    map = folium.Map(location=[unit.lat, unit.lon], zoom_start=13)
    map.add_to(figure)

    # Unit marker add to map
    folium.CircleMarker(
        location=[unit.lat, unit.lon],
        radius=10,
        popup="#" + str(unit.n_mt),
        color="#097969",
        fill=True,
        fill_color="#3186cc",
    ).add_to(map)

    # Customer marker's and path add to map
    for customer in customers:
        folium.CircleMarker(
            location=[customer.lat, customer.lon],
            radius=10,
            popup=customer.street + ", " + str(customer.building),
            color="#FF5733",
            fill=True,
            fill_color="#3186cc",
        ).add_to(map)
        # Draw path
        folium.PolyLine([[customer.lat, customer.lon], [unit.lat, unit.lon]]).add_to(
            map
        )

    figure.render()

    context = {"map": figure, "address": str(unit.address), "n_mt": unit.n_mt}
    return render(request, "map/unit.html", context)

# Пустая карта
def clear_map(request):
    val = request.GET.get("q")
    if val:
        try:
            # If unit not exists
            exists = Unit.objects.filter(n_mt=val)
            if not exists:
                return render(request, "map/unit_not_exists.html")
        except:
            return render(request, "map/unit_not_exists.html")

        figure = folium.Figure()
        unit = Unit.objects.get(n_mt=val)
        customers = Customer.objects.filter(unit=unit)

        map = folium.Map(location=[unit.lat, unit.lon], zoom_start=13)
        map.add_to(figure)

        # Unit marker add to map
        folium.CircleMarker(
            location=[unit.lat, unit.lon],
            radius=10,
            popup="#" + str(unit.n_mt),
            color="#097969",
            fill=True,
            fill_color="#3186cc",
        ).add_to(map)

        # Customer marker's and path add to map
        for customer in customers:
            folium.CircleMarker(
                location=[customer.lat, customer.lon],
                radius=10,
                popup=customer.street + ", " + str(customer.building),
                color="#FF5733",
                fill=True,
                fill_color="#3186cc",
            ).add_to(map)
            # Draw path
            folium.PolyLine(
                [[customer.lat, customer.lon], [unit.lat, unit.lon]]
            ).add_to(map)

        figure.render()

        context = {"map": figure, "address": unit.address, "n_mt": unit.n_mt}
        return render(request, "map/unit.html", context)

    figure = folium.Figure()

    map = folium.Map(location=[53.761683, 87.125225], zoom_start=13)
    map.add_to(figure)

    figure.render()

    context = {"map": figure, "address": "г.Новокузнецк", "n_mt": "backend app"}
    return render(request, "map/unit.html", context)
