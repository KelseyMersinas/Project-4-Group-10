# dictionary to hold the indexed values and their category values
values_to_index = {
    'cap_shape': {'Bell': 0, 'Conical': 1, 'Convex': 2, 'Flat': 3, 'Sunken': 4, 'Spherical': 5, 'Others': 6},
    'gill_attachment': {"Adnate": 0, 'Adnexed': 1, "Decurrent": 2, "Free": 3, "Sinuate": 4, "Pores":5, "None": 6},
    'season': {'Spring': 0.027372133055605714, "Summer": 0.8884502877862838, 'Fall': 0.9431945538974952, 'Winter': 1.8042727086281731},
    'stem_color': {"Brown": 0, "Buff": 1, "Gray": 2, "Green": 3, "Pink": 4, "Purple": 5, "Red": 6, "White": 7, "Yellow": 8, "Blue": 9, "Orange": 10, "Black": 11},
    'gill_color': {"Brown": 0, "Buff": 1, "Gray": 2, "Green": 3, "Pink": 4, "Purple": 5, "Red": 6, "White": 7, "Yellow": 8, "Blue": 9, "Orange": 10, "Black": 11}
}

# function to convert values in form back to index values in model
def convert_to_index(category, value):
    if category in values_to_index:
        if value in values_to_index[category]:
            return values_to_index[category][value]
        else:
            raise ValueError(f"Value '{value}' not found in category '{category}'")
    else:
        raise ValueError(f"Category '{category}' not found")