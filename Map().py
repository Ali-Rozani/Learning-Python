gaming_store = [("Nvidia RTX 4090 Super",137),
                            ("Intel Core I9 26 Cores",124),
                            ("8K High Resolution Monitor 16:9 530Hz",130)]
to_euros = lambda data: (data[0],data[1]*0.95)
store_euros = list(map(to_euros, gaming_store))
for i in store_euros:
    print(i)