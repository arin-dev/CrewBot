# filtered_data = [{'Director': {'UserId': 'emily.roberts@gmail.com', 'Preferred_because': "Emily Roberts has extensive experience (15 years) in visual storytelling and scene setup, which are crucial for a vlog. Her expertise in actor direction will ensure high-quality scenes, and her rate is within the project's budget."}}, {'Camera Operator': {'UserId': 'omar.almahmoud@gmail.com', 'Preferred_because': "Omar Al-Mahmoud has strong expertise in Camera Operation and Frame Composition, which are crucial for capturing high-quality vlog footage. Additionally, his rate is within a reasonable range for the project's budget, and he is located in Dubai, ensuring no additional travel costs."}}, {'Camera Operator': {'UserId': 'omar.almahmoud@gmail.com', 'Preferred_because': "Omar Al-Mahmoud has relevant expertise in Camera Operation and Frame Composition, which are crucial for capturing high-quality vlog footage. His rate is also within a reasonable range for the project's budget, and he is based in Dubai, ensuring no additional travel costs."}}]

# import sqlite3

# conn = sqlite3.connect('./DEMO_DB/crewdata.db')
# c = conn.cursor()
# selected_crews = {}
# for dictionary in filtered_data:
#     print(dictionary)
#     for key, val in dictionary.items():
#         print("##################### \n")
#         print("key", key, "val", val)
#         user = val
#         c.execute(f"SELECT * FROM 'crewdata' WHERE userid = \'{user['UserId']}\'")
#         user_details = c.fetchall()
#         print(user_details)
#         print("##################### \n")
#         role = key
#         if role not in selected_crews:
#             selected_crews[role] = []
#         selected_crews[role].append({
#             "name": user_details[0][0],
#             "userid": user_details[0][1],
#             "preferred_because": user['Preferred_because'],
#             "roleJobTitle": user_details[0][3],
#             "yoe": user_details[0][7],
#             "minRatePerDay": user_details[0][8],
#             "maxRatePerDay": user_details[0][9],
#             "location": user_details[0][10]
#         })
# conn.close()
# print("##################### \n")
# print(selected_crews)