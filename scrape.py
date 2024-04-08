import pandas as pd

states = ["California", "Texas", "Florida", "New York"]
population = [39250017, 27862596, 20612439, 19745289]

dict_state= {'States': states, 'Population': population}

df_states = pd.DataFrame.from_dict(dict_state)
print(df_states)
df_states.to_csv('states.csv', index=False)

#print(states[-4])

# for state in states:
#     if state == "Florida":
#         print(state)

# with open('test.txt', 'w') as file:
#     file.write("Data Successfully Scraped!")