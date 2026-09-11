import numpy as np
import numpy.typing as npt

from coordinate_conversions import rae_xyz

# some terms
# z_n               measured state vector at a time step n
# xhat_n,n          estimated system state vector at any time step n
# xhat_n+1,n        predicated system state vector at any time step n
# u_n               control variable or input variable representing known external inputs to the system
# F                 state transition matrix
# G                 control matrix or input matrix which maps an input to a state vector
# P_n,n             covariance matrix of the current state
# P_n+1,n           covariance matrix of the predicated state
# Q                 process noise matrix
# H                 observation matrix which maps a state variable to the measured system
# p_n,n-1           predicted state variance
# r_n               measurement variance

###################################################
# Kalman Filter

def generate_process_noise_matrix(x_variance: float, y_variance: float, z_variance: float, 
    vx_variance: float, vy_variance: float, vz_variance: float) -> npt.NDArray[any]:
    """Returns a process noise (covariance) matrix from the variances of various values.

    Keyword Args:
        x_variance -- the variance in the x measurement
        y_variance -- the vriance in the y measurement
        z_variance -- the variance in the z measurement
        vx_variance -- the variance in the x velocity measurement
        vy_variance -- the variance in the y velocity measurement
        vz_variance -- the variance in the z velocity measurement
    """
    # TODO: very simple and conceptual version
    process_noise_matrix = np.array([
        [ x_variance, 0, 0, 0, 0, 0 ],
        [ 0, y_variance, 0, 0, 0, 0 ],
        [ 0, 0, z_variance, 0, 0, 0 ],
        [ 0, 0, 0, vx_variance, 0, 0 ],
        [ 0, 0, 0, 0, vy_variance, 0 ],
        [ 0, 0, 0, 0, 0, vz_variance ]
    ])
    return process_noise_matrix

def generate_process_noise_from_matrix(process_noise_matrix: npt.NDArray[any]) -> npt.NDArray[any]:
    """Returns a process noise sample from a process noise matrix.

    Keyword Args:
        process_noise_matrix -- the covariance matrix describing the process noise distribution
    """
    rng = np.random.default_rng(seed=42)
    samples = rng.multivariate_normal([ 0, 0, 0, 0, 0, 0 ], process_noise_matrix)

    return samples

def generate_initial_statevector(measurement_0, measurement_1, delta_time: float) -> npt.NDArray[any]:
    """Returns an initial xyzv statevector from two RAER' measurements and a time difference.
    Measurements are expected to be of the form: [ range, azimuth, elevation, range rate ]

    Keyword Args:
        measuremenet_0 -- a chronologically earlier RAER' measurement
        measurement_ 1 -- a chronologically later RAER' measurement
        delta_time -- the time difference between both measurements
    """

    # Generate XYZ positions from the RAE components of the measurements
    measurement_0_xyz = rae_xyz(tuple(measurement_0[:3]))
    measurement_1_xyz = rae_xyz(tuple(measurement_1[:3]))

    x0, y0, z0 = measurement_0_xyz
    x1, y1, z1 = measurement_1_xyz

    vx = (x1 - x0) / delta_time
    vy = (y1 - y0) / delta_time
    vz = (z1 - z0) / delta_time

    initial = np.array([x1, y1, z1, vx, vy, vz ])
    return initial

def predict_statevector(current: npt.NDArray[any], process_noise, delta_time: float):
    """Predicts a statevector using the state extrapolation equation from some current statevector, process noise, and the
    time step between the current statevector and the predicted statevector.

    Keyword Args:
        current -- the current statevector
        process_noise -- the process noise
        delta_time -- the time step between statevectors
    """

    # The predicted statevector is given by the state extrapolation:
    # xhat_n+1,n = F xhat_n,n + G u_n + w_n
    # predicted state = transition matrix * current state + input transition matrix * input variable + process noise
    # NOTE: for now we are ignoring input variables

    # transition matrix for a constant velocity xyzv model is given by:
    transition = np.array([
        [ 1, 0, 0, delta_time, 0, 0 ],      # x_n+1 = x_n + v_n * Δt
        [ 0, 1, 0, 0, delta_time, 0 ],      # y_n+1 = y_n + v_y * Δt
        [ 0, 0, 1, 0, 0, delta_time ],      # z_n+1 = z_n + v_z * Δt
        [ 0, 0, 0, 1, 0, 0 ],
        [ 0, 0, 0, 0, 1, 0 ],
        [ 0, 0, 0, 0, 0, 1 ]
    ])

    predicted = transition @ current + process_noise
    return predicted

def kalman_gain():
    """

    """

    # determine multivariate kalman gain from unscented kalman gain model:
    # K = P_xz S^-1

    pass

def update_statevector(measured, predicted, gain):
    """

    """

    # The updated statevector is given by:
    # xhat_n,n = xhat_n,n-1 + K_n (z_n - xhat,n,n-1)
    # updated state = predicated state + kalman gain * (measured state - predicated state)

    # the innovation is another name for the term: measured state - predicated state

    updated = predicted + gain @ (measured - predicted)
    return updated

def kalman():
    # covariance extrapolation:
    # P_n+1,n = F P_n,n F^T + Q



    # multivariate kalmain gain:
    # K_n = P_n,n-1 H^T (H P_n,n-1 H^T + R_n)^-1



    # one dimensional covariance update equation:
    # p_n,n = (1 - K_n)p_n,n-1



    # multivariate covariance update equation:
    # P_n,n = (I - K_n H)P_n,n-1 (I - K_n H)^T + K_n R_n K_n^T

    pass





# TESTING

z0 = [100, 0, 0, 10]
z1 = [105, 0, 0, 10]
dt = 0.5

initial_statevector = generate_initial_statevector(z0, z1, dt)
print(f'Initial Statevector: {initial_statevector}')

Q = generate_process_noise_matrix(1, 1, 1, 2, 2, 2)
w = generate_process_noise_from_matrix(Q)
print(f'Process Noise: {w}')

predicted_statevector = predict_statevector(initial_statevector, w, 0.5)
print(f'Predicted Statevector: {predicted_statevector}')