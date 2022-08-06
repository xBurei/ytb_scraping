import datetime as dt
import matplotlib.pyplot as plt
from ytb_videos_scrapper import release_dates, titles, views


x = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in release_dates]
y = views

plt.plot_date(x, y, linestyle='solid')
plt.xlabel("Release date")
plt.ylabel("Number of views (in millions)")

manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()
