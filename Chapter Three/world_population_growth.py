#3.27 (World Population Growth)
current_world_population = 8_200_000_000
ANNUAL_GROWTH_RATE = 0.85 / 100
annual_population_increase = current_world_population * ANNUAL_GROWTH_RATE
each_year_population = annual_population_increase + current_world_population
numerical_increase = each_year_population - current_world_population
print("Year\tWord Population\t Numerical Increase")
for number in range(100):
	print(f'{number: >4} \t {each_year_population: >8.0f} \t {numerical_increase: >10.0f}')
	current_population = each_year_population
	each_year_population = (each_year_population * ANNUAL_GROWTH_RATE) + each_year_population
	numerical_increase = each_year_population - current_population
	
if each_year_population == current_world_population * 2:
	print(number, each_year_population)

