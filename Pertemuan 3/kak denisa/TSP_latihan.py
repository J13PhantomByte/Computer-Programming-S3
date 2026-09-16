import random

# ==========================================
# 1. DATA KOTA
# ==========================================

cities = [
    (0, 0),
    (1, 2),
    (3, 1),
    (2, 4),
    (4, 3)
]


# ==========================================
# 2. FUNGSI JARAK
# ==========================================

def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2

    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


# ==========================================
# 3. TOTAL JARAK RUTE
# ==========================================

def total_distance(route):

    dist = 0

    for i in range(len(route) - 1):
        dist += distance(
            cities[route[i]],
            cities[route[i + 1]]
        )

    # Kembali ke kota awal
    dist += distance(
        cities[route[-1]],
        cities[route[0]]
    )

    return dist


# ==========================================
# 4. PARAMETER GENETIC ALGORITHM
# ==========================================

population_size = 10
num_generations = 100
mutation_rate = 0.1


# ==========================================
# 5. POPULASI AWAL
# ==========================================

population = [
    random.sample(range(len(cities)), len(cities))
    for _ in range(population_size)
]


# ==========================================
# 6. SIMPAN SOLUSI TERBAIK
# ==========================================

best_route = None
best_distance = float("inf")


# ==========================================
# 7. GENETIC ALGORITHM
# ==========================================

for generation in range(num_generations):

    # --------------------------------------
    # Evaluasi Fitness
    # --------------------------------------

    fitness_scores = [
        1 / total_distance(route)
        for route in population
    ]


    # --------------------------------------
    # Cek solusi terbaik generasi ini
    # --------------------------------------

    current_best = min(
        population,
        key=total_distance
    )

    current_distance = total_distance(current_best)


    # Simpan jika lebih baik
    if current_distance < best_distance:

        best_distance = current_distance
        best_route = current_best.copy()


    # --------------------------------------
    # Selection
    # Tournament Selection
    # --------------------------------------

    selected_routes = []

    for _ in range(population_size):

        tournament = random.sample(
            range(population_size),
            5
        )

        winner = max(
            tournament,
            key=lambda idx: fitness_scores[idx]
        )

        selected_routes.append(winner)


    # --------------------------------------
    # Crossover + Mutation
    # --------------------------------------

    new_population = []

    for i in range(0, population_size, 2):

        parent1 = population[selected_routes[i]]
        parent2 = population[selected_routes[i + 1]]


        # ----------------------------------
        # Simple Order Crossover
        # ----------------------------------

        point = random.randint(
            1,
            len(cities) - 1
        )

        child1 = (
            parent1[:point]
            + [
                city
                for city in parent2
                if city not in parent1[:point]
            ]
        )

        child2 = (
            parent2[:point]
            + [
                city
                for city in parent1
                if city not in parent2[:point]
            ]
        )


        # ----------------------------------
        # Mutation Child 1
        # ----------------------------------

        if random.random() < mutation_rate:

            m1, m2 = random.sample(
                range(len(cities)),
                2
            )

            child1[m1], child1[m2] = (
                child1[m2],
                child1[m1]
            )


        # ----------------------------------
        # Mutation Child 2
        # ----------------------------------

        if random.random() < mutation_rate:

            m1, m2 = random.sample(
                range(len(cities)),
                2
            )

            child2[m1], child2[m2] = (
                child2[m2],
                child2[m1]
            )


        new_population.extend([
            child1,
            child2
        ])


    # Populasi generasi berikutnya
    population = new_population


# ==========================================
# 8. HASIL AKHIR
# ==========================================

print("=== GA TSP OPTIMIZATION RESULT ===")

print(
    "Best Route Found (City Indices):",
    best_route
)

print(
    "Total Minimum Distance          :",
    round(best_distance, 4)
)