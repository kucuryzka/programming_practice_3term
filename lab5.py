import pandas as pd

print("step 1")
data = {
    "name": ["Strom, Mrs. Wilhelm (ElnaMatilda Persson)", "Navratil, Mr. Michel (Louis MHoffman)", "Minahan, Miss. Daisy E"],
    "age": [29, 36.5, 33],
    "sex": ["female", "male", "female"]
}

row_labels = [1, 2, 3]

df1 = pd.DataFrame(data=data, index=row_labels)

print(df1)


print("step 2")
df2 = pd.read_csv('titanic_csv.csv', sep=";")
df2.columns = df2.columns.str.lower()
print(df2)

print("step 3")
df3 = pd.read_csv('https://gist.githubusercontent.com/zaryanezrya/8b4ef51c707cb16d5e88a44dc00a1bb2/raw/41230f49c6268e072dbf102672f670be256922ab/gistfile1.txt', sep=",")
print(df3)

print("step 4")
df4 = pd.concat([df2, df3], ignore_index=True)
df4 = df4.drop_duplicates()
print(df4)

print("step5")
df4 = df4.set_index("passengerid")
df4 = df4.sort_index()


print(df4)

print("step 6")
print(df4.info)
print(df4.describe())


print("step 7")
df4.iloc[0], df4.loc[2] = df4.loc[2].copy(), df4.iloc[0].copy()
print(df4)

print("step 8")
df4["sex"] = df4["sex"].map({"female": "f", "male": "m"})
with pd.option_context('display.max_columns', None):
    print(df4)


print("step 9")
ticket_counts = df4.groupby("ticket")["ticket"].count()

large_tickets = ticket_counts[ticket_counts >= 6]

for ticket_name in large_tickets.index:
    group = df4[df4["ticket"] == ticket_name]
    print("Билет:", ticket_name)
    print(f"Количество людей: {large_tickets[ticket_name]}")
    print(group[["name", "age", "sex", "pclass"]].to_string(index=False))
    print("\n")


print("step 10")
for el in df1.iterrows():
    person_name = el[1]["name"]
    person_cabin = df4[df4["name"] == person_name]
    if not person_cabin.empty:
        cabin = person_cabin["cabin"].to_string(index=False, header=False)

        print(f"Люди из одной каюты с {person_name}")
        print(df4[df4["cabin"] == cabin])


print("step 11")
df4["birthyear"] = [1920 - el[1]["age"] for el in df4.iterrows()]
print(df4)


print("step 12")
companion_num = []
for el in df4.iterrows():
    filtered = df4[df4["cabin"] == el[1]["cabin"]]
    companion_num.append(filtered.size)

df4["companion"] = companion_num
print(df4)


print("step 13")
df4.iloc[0], df4.loc[1] = df4.loc[1].copy(), df4.iloc[0].copy()
print(df4)

print("step  14")
df4.to_csv("result.csv")

print("step 15")
top_prices = df4.nlargest(n=10, columns="fare")
print(top_prices)

print("step 16")
surv_f = df4[(df4["sex"] == "f") & (df4["survived"] == 1)].shape[0]
unsurv_f = df4[(df4["sex"] == "f") & (df4["survived"] == 0)].shape[0]
surv_m = df4[(df4["sex"] == "m") & (df4["survived"] == 1)].shape[0]
unsurv_m = df4[(df4["sex"] == "m") & (df4["survived"] == 0)].shape[0]


print(f"Женщины: выжило {surv_f}, не выжило {unsurv_f}")
print(f"Мужчины: выжило {surv_m}, не выжило {unsurv_m}")


print("step 17")
for pclass in set(df4["pclass"].values):
    surv = df4[(df4["pclass"] == pclass) & (df4["survived"] == 1)].shape[0]
    unsurv = df4[(df4["pclass"] == pclass) & (df4["survived"] == 0)].shape[0]

    print(f"Класс {pclass}: выжило {surv}, не выжило {unsurv}")

