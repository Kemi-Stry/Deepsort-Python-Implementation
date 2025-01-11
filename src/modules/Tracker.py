import numpy as np
import cv2 as cv

class Tracker:
   age: int

   def __init__(self):
      self.age = 0
      self.descriptors = []


      # Initialize the Kalman Filter
      kalman = cv.KalmanFilter(4, 2, 0)

      # Transition matrix ( A )
      kalman.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)

      # Measurement matrix ( H ) 
      kalman.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], np.float32)

      # Process noise covariance matrix ( Q )
      kalman.processNoiseCov = np.eye(4, dtype=np.float32) * 1e-4

      # Measurement noise covariance matrix ( R )
      kalman.measurementNoiseCov = np.eye(2, dtype=np.float32) * 1e-1

      # Estimate error covariance matrix ( P )
      kalman.errorCovPost = np.eye(4, dtype=np.float32) * 0.1

      # Initial state k
      kalman.statePost = np.array([[0], [0], [0], [0]], np.float32)

      # Random measurement input 
      measurement = np.array([[2], [3]], np.float32)

      # Prediction step 
      prediction = kalman.predict()

      # Update step 
      kalman.correct(measurement)