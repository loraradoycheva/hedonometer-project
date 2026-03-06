import pandas as pd


#For total 2015
df_claim_15 = pd.read_csv('data/cache/2015/claim_15.csv')
df_discuss_15 = pd.read_csv('data/cache/2015/discuss_15.csv')
df_report_15 = pd.read_csv('data/cache/2015/report_15.csv')
df_state_15 = pd.read_csv('data/cache/2015/state_15.csv')

df_2015 = pd.concat([df_claim_15, df_discuss_15, df_report_15, df_state_15], ignore_index=True, sort=False)
#df_2015.to_csv('data/cache/2015/data_2015.csv', index=False)

#For total 2016
df_claim_16 = pd.read_csv('data/cache/2016/claim_16.csv')
df_discuss_16 = pd.read_csv('data/cache/2016/discuss_16.csv')
df_report_16 = pd.read_csv('data/cache/2016/report_16.csv')
df_state_16 = pd.read_csv('data/cache/2016/state_16.csv')

df_2016 = pd.concat([df_claim_16, df_discuss_16, df_report_16, df_state_16], ignore_index=True, sort=False)
#df_2016.to_csv('data/cache/2016/data_2016.csv', index=False)

#For total 2017
df_claim_17 = pd.read_csv('data/cache/2017/claim_17.csv')
df_discuss_17 = pd.read_csv('data/cache/2017/discuss_17.csv')
df_report_17 = pd.read_csv('data/cache/2017/report_17.csv')
df_state_17 = pd.read_csv('data/cache/2017/state_17.csv')

df_2017 = pd.concat([df_claim_17, df_discuss_17, df_report_17, df_state_17], ignore_index=True, sort=False)
#df_2017.to_csv('data/cache/2017/data_2017.csv', index=False)

#For total 2018
df_claim_18 = pd.read_csv('data/cache/2018/claim_18.csv')
df_discuss_18 = pd.read_csv('data/cache/2018/discuss_18.csv')
df_report_18 = pd.read_csv('data/cache/2018/report_18.csv')
df_state_18 = pd.read_csv('data/cache/2018/state_18.csv')

df_2018 = pd.concat([df_claim_18, df_discuss_18, df_report_18, df_state_18], ignore_index=True, sort=False)
#df_2018.to_csv('data/cache/2018/data_2018.csv', index=False)

#For total 2019
df_claim_19 = pd.read_csv('data/cache/2019/claim_19.csv')
df_discuss_19 = pd.read_csv('data/cache/2019/discuss_19.csv')
df_report_19 = pd.read_csv('data/cache/2019/report_19.csv')
df_state_19 = pd.read_csv('data/cache/2019/state_19.csv')

df_2019 = pd.concat([df_claim_19, df_discuss_19, df_report_19, df_state_19], ignore_index=True, sort=False)
#df_2019.to_csv('data/cache/2019/data_2019.csv', index=False)

#For total 2020
df_claim_20 = pd.read_csv('data/cache/2020/claim_20.csv')
df_discuss_20 = pd.read_csv('data/cache/2020/discuss_20.csv')
df_report_20 = pd.read_csv('data/cache/2020/report_20.csv')
df_state_20 = pd.read_csv('data/cache/2020/state_20.csv')

df_2020 = pd.concat([df_claim_20, df_discuss_20, df_report_20, df_state_20], ignore_index=True, sort=False)
#df_2020.to_csv('data/cache/2020/data_2020.csv', index=False)

#For total 2021
df_claim_21 = pd.read_csv('data/cache/2021/claim_21.csv')
df_discuss_21 = pd.read_csv('data/cache/2021/discuss_21.csv')
df_report_21 = pd.read_csv('data/cache/2021/report_21.csv')
df_state_21 = pd.read_csv('data/cache/2021/state_21.csv')

df_2021 = pd.concat([df_claim_21, df_discuss_21, df_report_21, df_state_21], ignore_index=True, sort=False)
#df_2021.to_csv('data/cache/2021/data_2021.csv', index=False)

#For total 2022
df_claim_22 = pd.read_csv('data/cache/2022/claim_22.csv')
df_discuss_22 = pd.read_csv('data/cache/2022/discuss_22.csv')
df_report_22 = pd.read_csv('data/cache/2022/report_22.csv')
df_state_22 = pd.read_csv('data/cache/2022/state_22.csv')

df_2022 = pd.concat([df_claim_22, df_discuss_22, df_report_22, df_state_22], ignore_index=True, sort=False)
#df_2022.to_csv('data/cache/2022/data_2022.csv', index=False)

#For total 2023
df_claim_23 = pd.read_csv('data/cache/2023/claim_23.csv')
df_discuss_23 = pd.read_csv('data/cache/2023/discuss_23.csv')
df_report_23 = pd.read_csv('data/cache/2023/report_23.csv')
df_state_23 = pd.read_csv('data/cache/2023/state_23.csv')

df_2023 = pd.concat([df_claim_23, df_discuss_23, df_report_23, df_state_23], ignore_index=True, sort=False)
#df_2023.to_csv('data/cache/2023/data_2023.csv', index=False)

#For total 2024
df_claim_24 = pd.read_csv('data/cache/2024/claim_24.csv')
df_discuss_24 = pd.read_csv('data/cache/2024/discuss_24.csv')
df_report_24 = pd.read_csv('data/cache/2024/report_24.csv')
df_state_24 = pd.read_csv('data/cache/2024/state_24.csv')

df_2024 = pd.concat([df_claim_24, df_discuss_24, df_report_24, df_state_24], ignore_index=True, sort=False)
#df_2024.to_csv('data/cache/2024/data_2024.csv', index=False)

#For total 2025
df_claim_25 = pd.read_csv('data/cache/2025/claim_25.csv')
df_discuss_25 = pd.read_csv('data/cache/2025/discuss_25.csv')
df_report_25 = pd.read_csv('data/cache/2025/report_25.csv')
df_state_25 = pd.read_csv('data/cache/2025/state_25.csv')

df_2025 = pd.concat([df_claim_25, df_discuss_25, df_report_25, df_state_25], ignore_index=True, sort=False)
#df_2025.to_csv('data/cache/2025/data_2025.csv', index=False)



df_2015_2019 = pd.concat([df_2015, df_2016, df_2017, df_2018, df_2019], ignore_index=True, sort=False)
#df_2015_2019.to_csv('data/cache/data_2015_2019.csv', index=False)

df_2020_2025 = pd.concat([df_2020, df_2021, df_2022, df_2023, df_2024, df_2025], ignore_index=True, sort=False)
#df_2020_2025.to_csv('data/cache/data_2020_2025.csv', index=False)


df_all = pd.concat([df_2015, df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022, df_2023, df_2024, df_2025], ignore_index=True, sort=False)
#df_all.to_csv('data/cache/data_all.csv', index=False)