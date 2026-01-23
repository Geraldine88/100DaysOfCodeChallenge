import pandas as pd

# FIGURE OUT HOW MANY SQUIRRELS THERE ARE PER EACH COLOR

sq_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260122.csv")
prim_color = sq_data["Primary Fur Color"]
unique_colors = prim_color.dropna().unique()
print(unique_colors)

gray_sq = (prim_color == 'Gray').sum()
cinnamon_sq = (prim_color == 'Cinnamon').sum()
black_sq = (prim_color == 'Black').sum()

# print(f'Gray Squirrel Count: {gray_sq}')
# print(f'Cinnamon Squirrel Count: {cinnamon_sq}')
# print(f'Black Squirrel Count: {black_sq}')

sq_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count' : [gray_sq, cinnamon_sq, black_sq]
}

sq_df = pd.DataFrame(sq_dict)
sq_df.to_csv("squirrel_counts.csv", index=False)
