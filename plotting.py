import datetime as dt
import matplotlib.pyplot as plt
from ytb_videos_scrapper import release_dates, titles, views
import mplcursors

x = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in release_dates]
y = views

point_data = []
for i in range (0, len(y)):
	temp = [x[i], y[i], titles[i]]

fig = plt.figure()
ax = fig.add_subplot(111)

sc = plt.scatter(x, y)
ax.set_ylim(bottom=0)
plt.xlabel("Release date")
if type(y[0]) is float:
	plt.ylabel("Number of views (in millions)")
else:
	plt.ylabel("Number of views")

manager = plt.get_current_fig_manager()
manager.full_screen_toggle()

#annotations
annotation = ax.annotate(
	text='',
	xy=(0, 0),
	xytext=(5, 5),
	textcoords='offset points',
	bbox={'boxstyle': 'round', 'fc': 'w'},
	arrowprops={'arrowstyle': '->'}
)

annotation.set_visible(False)

def update_annot(ind):
	index = ind["ind"][0]
	pos = sc.get_offsets()[ind["ind"][0]]
	annotation.xy = pos
	v = '{:,}'.format(views[index])
	text = str(x[index]) + "\n" + v + "\n" + titles[index]
	annotation.set_text(text)

def on_hover(event):
	vis = annotation.get_visible()
	if event.inaxes == ax:
		cont, ind = sc.contains(event)
		if cont:
			update_annot(ind)
			annotation.set_visible(True)
			fig.canvas.draw_idle()
		elif vis:
			annotation.set_visible(False)
			fig.canvas.draw_idle()




fig.canvas.mpl_connect("motion_notify_event", on_hover)

plt.show()
