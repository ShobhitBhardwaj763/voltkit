
from voltkit.core import load_csv_signal, plot_signal

t,y = load_csv_signal("C:/sample_dataset/sample.csv")

t,y1 = load_csv_signal("C:/sample_dataset/sample.csv", column=2)

plot_signal(t,y, title="Sample")
plot_signal(t,y1, title="Sample2")
