number_of_locations, number_of_roads = map(int, input().split())
print(f"{number_of_roads=}, {number_of_locations=}")


assert 2 <= number_of_locations <= 10**5
assert (
    number_of_locations - 1
    <= number_of_roads
    <= min(2 * 10**5, number_of_locations * (number_of_locations - 1) / 2)
)
for i in range(number_of_roads):
    a, b, c = map(int, input().split())
    print(f"{a=}, {b=}, {c=}")
