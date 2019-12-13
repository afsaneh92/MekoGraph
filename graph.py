import datetime as dt
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def main():
    # Create figure for plotting
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    xs = []
    ys = []


    # This function is called periodically from FuncAnimation
    def animate(i, xs, ys):

        temp_c = random.randrange(3, 9)

        # Add x and y to lists
        xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        ys.append(temp_c)

        # Limit x and y lists to 20 items
        xs = xs[-20:]
        ys = ys[-20:]

        # Draw x and y lists
        ax.clear()
        ax.plot(xs, ys)

        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('Y over Time')
        plt.ylabel('Y')

    # Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
    plt.show()


    # from pylab import *
    #
    # t = arange(0.0, 2.0, 0.01)
    # s = sin(2 * pi * t)
    # plot(t, s, linewidth=1.0)
    #
    # xlabel('time (s)')
    # ylabel('voltage (mV)')
    # title('About as simple as it gets, folks')
    # grid(True)
    # show()

if __name__ == '__main__':
    main()