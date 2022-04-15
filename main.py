import cv2
import matplotlib.pyplot as plt
from measurement import create_circle_data
from KalmanFilter import ExtendedKalmanFilter
from KalmanFilter import LinearKalmanFilter
import math
#this function takes in the filter object and measurements as arguments. This function call the predit and update methods of the object and adds the result in result
def action(filter, measurements):
    result = []
    count=0
    

    for i in range(len(measurements)):
        count+=1
        m = measurements[i]
        filter.predict()
        if(count%6==0):
            filter.update(m)
        pred=filter.x[0:2, :].flatten()
        result.append(pred)

    return result
#function to plot and visualize our results
def plot(measurements, result,result1, radius):
    plt.figure("Kalman Filter Visualization")
    plt.subplot(211)
    plt.scatter([x[0] for x in measurements], [x[1] for x in measurements], c='red', label='Real Position', alpha=0.3, s = 4)
    plt.scatter([x[0] for x in result], [x[1] for x in result], c='blue', label='Predicted Position', alpha=0.3, s = 4, marker='x')
    plt.legend()
    plt.grid('on')
    plt.title("Linear Kalman Fiter")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.xlim(-radius, radius)
    plt.ylim(-radius, radius)
    plt.subplot(212)
    plt.scatter([x[0] for x in measurements], [x[1] for x in measurements], c='red', label='Real Position', alpha=0.3, s = 4)
    plt.scatter([x[0] for x in result1], [x[1] for x in result1], c='blue', label='Predicted Position', alpha=0.3, s = 4, marker='x')
    plt.legend()
    plt.grid('on')
    plt.title("Extended Kalman Filter")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.xlim(-radius, radius)
    plt.ylim(-radius, radius)
    plt.tight_layout()
    plt.show()


def main():
    #options for step_size, radius of circle and no of rounds
    options = {
        'step_size': 0.1,
        'radius': 400,
        'N': 1,
    }
    #create LinearKalmanFilter Object
    filter = LinearKalmanFilter(sigma=1)
    #create ExtendedKalmanFIlter Object
    filter1 = ExtendedKalmanFilter(sigma=1)
    #get measurement values
    measurements = create_circle_data(**options)
    #get predicted position data for LinearKalmanFilter
    result = action(filter, measurements)
    #get predicted position data for ExtendedKalmanFilter
    result1 = action(filter1, measurements)
    #plot data
    plot(measurements,result, result1, radius = options['radius']*2)
#execute main
if __name__ == '__main__':
    main()
#this function takes in the filter object and measurements as arguments. This function call the predit and update methods of the object and adds the result in result
def action(filter, measurements):
    result = []
    count=0
    

    for i in range(len(measurements)):
        count+=1
        m = measurements[i]
        filter.predict()
        if(count%6==0):
            filter.update(m)
        pred=filter.x[0:2, :].flatten()
        result.append(pred)

    return result
#function to plot and visualize our results
def plot(measurements, result,result1, radius):
    plt.figure("Kalman Filter Visualization")
    plt.subplot(211)
    plt.scatter([x[0] for x in measurements], [x[1] for x in measurements], c='red', label='Real Position', alpha=0.3, s = 4)
    plt.scatter([x[0] for x in result], [x[1] for x in result], c='blue', label='Predicted Position', alpha=0.3, s = 4, marker='x')
    plt.legend()
    plt.grid('on')
    plt.title("Linear Kalman Fiter")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.xlim(-radius, radius)
    plt.ylim(-radius, radius)
    plt.subplot(212)
    plt.scatter([x[0] for x in measurements], [x[1] for x in measurements], c='red', label='Real Position', alpha=0.3, s = 4)
    plt.scatter([x[0] for x in result1], [x[1] for x in result1], c='blue', label='Predicted Position', alpha=0.3, s = 4, marker='x')
    plt.legend()
    plt.grid('on')
    plt.title("Extended Kalman Filter")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.xlim(-radius, radius)
    plt.ylim(-radius, radius)
    plt.tight_layout()
    plt.show()



