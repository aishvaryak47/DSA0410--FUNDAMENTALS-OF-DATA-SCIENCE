import numpy as np

car_models = ["Model A", "Model B", "Model C", "Model D", "Model E"]
fuel_efficiency = np.array([22.5, 28.0, 31.4, 25.6, 35.2])   # miles per gallon

average_mpg = np.mean(fuel_efficiency)
print(f"Average fuel efficiency: {average_mpg:.2f} mpg")

# Compare two models (change these indexes to compare other models)
old_model, new_model = 0, 4
improvement = (fuel_efficiency[new_model] - fuel_efficiency[old_model]) / fuel_efficiency[old_model] * 100
print(f"{car_models[old_model]}: {fuel_efficiency[old_model]} mpg, "
      f"{car_models[new_model]}: {fuel_efficiency[new_model]} mpg")
print(f"Improvement of {car_models[new_model]} over {car_models[old_model]}: {improvement:.2f}%")
