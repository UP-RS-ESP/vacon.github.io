#!/usr/bin/env python

import numpy as np
import pandas as pd
import os, glob, tqdm, sys
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.dates import AutoDateLocator
import matplotlib.dates as mdates
from dateutil.tz import gettz

data_path = sys.argv[1]
station_name = sys.argv[2]
file_prefix = sys.argv[3]

# station_name='KNP1'
# data_path='/home/bodo/Dropbox/India_Nov2023/clim_data/knp1'
filelist1 = glob.glob(os.path.join(data_path, "*/*.gz"))
filelist2 = glob.glob(os.path.join(data_path, "*.gz"))
filelist = filelist1 + filelist2
filelist.sort()

dfs = []
for name in tqdm.tqdm(filelist):
    df = pd.read_csv(
        name,
        sep=",",
        skipinitialspace=True,
        skiprows=1,
        skip_blank_lines=True,
        names=[
            "date",
            "T1_C",
            "T1_C_sd",
            "T2_C",
            "T2_C_sd",
            "rh",
            "rh_sd",
            "P_hpa",
            "P_hpa_sd",
            "Elev_m",
            "Elev_m_sd",
            "nr_meas",
        ],
    )
    df["date"] = pd.to_datetime(df["date"], utc=True, format="ISO8601")
    dfs.append(df)

df_all = pd.concat(dfs, ignore_index=True)
df_all.set_index("date", inplace=True)
df_all.drop(df_all[df_all.nr_meas < 5].index, inplace=True)
df_all.drop(df_all[df_all.T1_C_sd > 1].index, inplace=True)
df_all.drop(df_all[df_all.P_hpa_sd > 2].index, inplace=True)
df_all.drop(df_all[df_all.T2_C_sd > 1].index, inplace=True)
df_all.drop(df_all[df_all.rh_sd > 5].index, inplace=True)
df_all.drop(df_all[df_all.rh_sd > 5].index, inplace=True)
df_all.sort_index(ascending=True, inplace=True)
# Drop NaT rows
df_all["TMP"] = df_all.index.values  # index is a DateTimeIndex
df_all_noNat = df_all[df_all.TMP.notnull()].copy()  # remove all NaT values
df_all_noNat.drop(["TMP"], axis=1, inplace=True)
# df_all[df_all.index.isnull()]
df_all = df_all_noNat.copy()
df_all_noNat = None

df_all["rh_10m_rolling_average"] = df_all["rh"].rolling("10min").mean()
df_all["P_hpa_10m_rolling_average"] = df_all["P_hpa"].rolling("10min").mean()

fg, ax = plt.subplots(
    nrows=2, ncols=1, figsize=(12, 10), dpi=300, layout="constrained", sharex=True
)
ax[0].errorbar(
    x=df_all.index,
    y=df_all["T1_C"],
    yerr=df_all["T1_C_sd"],
    linestyle="",
    marker="o",
    ms=1,
    lw=0.5,
    color="navy",
    label="T1 (outside)",
)
ax[0].errorbar(
    x=df_all.index,
    y=df_all["T2_C"],
    yerr=df_all["T2_C_sd"],
    linestyle="",
    marker="o",
    ms=1,
    lw=0.5,
    color="darkred",
    label="T2 (inside)",
)
ax[0].grid()
# ax[0].set_xlabel("Month-Day: Hour (GMT)")
ax[0].set_ylabel(r"Temperature ($^\circ$C)")
ax[0].legend()
date_form = DateFormatter("%b-%d: %H")
date_form.set_tzinfo(gettz("GMT"))
ax[0].xaxis.set_major_formatter(date_form)
ax[0].xaxis.set_major_locator(mdates.HourLocator(interval=24))
start_time = np.max(df_all.index) - np.timedelta64(10, "D")
start_time.replace(hour=0, minute=0, second=0, microsecond=0)
end_time = np.max(df_all.index)
end_time.replace(hour=23, minute=59, second=59, microsecond=0)
ax[0].set_xlim([start_time, end_time])
ax[0].set_title(
    "%s: 1-minute logging interval, temperature" % station_name, fontsize=16
)

ax1b = ax[1].twinx()
lns1 = ax[1].errorbar(
    x=df_all.index,
    y=df_all["P_hpa"],
    yerr=df_all["P_hpa_sd"],
    linestyle="",
    lw=0.5,
    color="lightgreen",
    label="Pressure",
)
lns2 = ax1b.errorbar(
    x=df_all.index,
    y=df_all["rh"],
    yerr=df_all["rh_sd"],
    linestyle="",
    lw=0.5,
    color="violet",
    label="Rel. Humidity",
)
ax1b.plot(
    df_all.index,
    df_all["rh_10m_rolling_average"],
    marker="o",
    ms=1,
    linestyle="",
    color="purple",
    label="Rel. Humidity, 10-min rolling mean",
)
ax[1].plot(
    df_all.index,
    df_all["P_hpa_10m_rolling_average"],
    marker="o",
    ms=1,
    linestyle="",
    color="darkgreen",
    label="Pressure, 10-min rolling mean",
)
ax[1].grid()
ax[1].set_xlabel("Month-Day-Hour (GMT)")
ax[1].set_ylabel("Pressure (hPa)")
ax1b.set_ylabel("Rel. Humidity (%)")
lines, labels = ax[1].get_legend_handles_labels()
lines2, labels2 = ax1b.get_legend_handles_labels()
ax1b.legend(lines + lines2, labels + labels2, loc=0)
ax[1].xaxis.set_major_formatter(date_form)
ax[1].xaxis.set_major_locator(mdates.HourLocator(interval=24))
ax[1].xaxis.set_minor_locator(mdates.HourLocator(interval=12))
ax[1].set_title("%s: pressure and relative humidity" % station_name, fontsize=16)
ax[1].set_xlim([start_time, end_time])
# ax[1].set_xlim([np.max(df_all.index) - np.timedelta64(10,'D'), np.max(df_all.index)])
fg.savefig("%s_TempP_last10days.png" % file_prefix, dpi=300)
plt.close(fg)


fg, ax = plt.subplots(nrows=2, ncols=1, figsize=(12, 10), dpi=300, layout="constrained")
ax[0].errorbar(
    x=df_all.index,
    y=df_all["T1_C"],
    yerr=df_all["T1_C_sd"],
    linestyle="",
    marker="o",
    ms=0.5,
    lw=0.2,
    color="navy",
    label="T1 (outside)",
)
ax[0].grid()
# ax[0].set_xlabel("Year.Month.Day")
ax[0].set_ylabel(r"Temperature ($^\circ$C)")
ax[0].legend()
date_form = DateFormatter("%Y.%m.%d")
date_form.set_tzinfo(gettz("GMT"))
ax[0].xaxis.set_major_formatter(date_form)
end_time = np.max(df_all.index)
end_time.replace(hour=23, minute=59, second=59, microsecond=0)
ax[0].set_title("%s: 1-minute logging interval, temperature" % station_name)

ax1b = ax[1].twinx()
lns1 = ax[1].errorbar(
    x=df_all.index,
    y=df_all["P_hpa"],
    yerr=df_all["P_hpa_sd"],
    linestyle="",
    lw=0.1,
    color="lightgreen",
    label="Pressure",
)
lns2 = ax1b.errorbar(
    x=df_all.index,
    y=df_all["rh"],
    yerr=df_all["rh_sd"],
    linestyle="",
    lw=0.1,
    color="violet",
    label="Rel. Humidity",
)
ax1b.plot(
    df_all.index,
    df_all["rh_10m_rolling_average"],
    marker="o",
    ms=0.5,
    linestyle="",
    color="purple",
    label="Rel. Humidity, 10-min rolling mean",
)
ax[1].plot(
    df_all.index,
    df_all["P_hpa_10m_rolling_average"],
    marker="o",
    ms=0.5,
    linestyle="",
    color="darkgreen",
    label="Pressure, 10-min rolling mean",
)
ax[1].grid()
ax[1].set_xlabel("Year.Month.Day")
ax[1].set_ylabel("Pressure (hPa)")
ax1b.set_ylabel("Rel. Humidity (%)")
lines, labels = ax[1].get_legend_handles_labels()
lines2, labels2 = ax1b.get_legend_handles_labels()
ax1b.legend(lines + lines2, labels + labels2, loc=0)
ax[1].xaxis.set_major_formatter(date_form)
# ax[1].xaxis.set_major_locator(mdates.HourLocator(interval=12))
# ax[1].xaxis.set_minor_locator(mdates.HourLocator(interval=6))
ax[1].set_title("Station %s: pressure and relative humidity" % station_name)
# ax[1].set_xlim([np.max(df_all.index) - np.timedelta64(5,'D'), np.max(df_all.index)])
fg.savefig("%s_TempP.png" % file_prefix, dpi=300)
plt.close(fg)
