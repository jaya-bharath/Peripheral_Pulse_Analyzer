"""calculate the features of Peripheral Pulse Analyzer (PPA) waveforms"""
import pathlib
import pandas as pd
import matplotlib.pyplot as plt
import scipy

if __name__ == "__main__":
    # read txt files
    path = pathlib.Path(__file__).parent.parent / "data"
    files = path.glob("*.txt")

    # read into pandas dataframe
    df = pd.concat((pd.read_csv(f, names=["Amplitude"], nrows=3000) for f in files), ignore_index=True)

    print(df.idxmax())
    print(df.max())
    # print(df.count())

    # print(df[df["Amplitude"] == 141])

    # find Peaks
    df_peaks, _ = scipy.signal.find_peaks(df["Amplitude"])
    peaks_ = df["Amplitude"][df_peaks]
    print(peaks_)

    # plot graph
    head = df["Amplitude"]
    plt.plot(head)
    plt.plot(df_peaks, head[df_peaks], "x")
    plt.title("PPA")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.show()
    plt.close()
