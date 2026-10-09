#quick note : this is in a class to make sure it is easily accessible to other functions
#and keep in mind in Py classes do not have the privacy of C++ classes. So we use the __ to create it ourselves.

import time

class Control: 
    # NOTE: double underscores (name mangling) used for greater security on essential multipliers
    def __init__(self, kp, ki, kd, integral = 0, prev_error = 0, prev_time = 0):
        """
        Initialize class members.

        Keyword Args:
            kp -- proportional multipler
            ki -- integral multiplier
            kd -- derivative multiplier
            integral -- integral accumulator for PID calculations
            prev_error -- a seed error to use for PID calculations
            prev_time -- a seed time in seconds on the monotonic clock; 0 means
                         "not yet seeded" and makes the constructor stamp the
                         current time.
        """

        self.__kp = kp 
        self.__ki = ki 
        self.__kd = kd
        self.__integral = integral
        self.__prev_error = prev_error
        # A zero prev_time means the caller has not seeded the clock, not that
        # the loop started at time zero. Seeding it here keeps the first call's
        # dt at one control period instead of the machine's entire uptime;
        # otherwise the first integral update multiplies the error by the uptime
        # and saturates the actuator.
        self.__prev_time = time.monotonic() if prev_time == 0 else prev_time

    ###################################################
        
    # NOTE: read only for when needed to access the values of kp, ki, kd, integral, prev_error, and prev_time.
    @property
    def kp(self): 
        return self.__kp 
    @property
    def ki(self): 
        return self.__ki 
    @property
    def kd(self): 
        return self.__kd 
    @property 
    def integral(self): 
        return self.__integral
    @property
    def prev_error(self): 
        return self.__prev_error
    @property
    def prev_time(self): 
        return self.__prev_time
    
    ###################################################

    # NOTE: to access kp, ki, or kd, you still use kp ki and kd outside the class. IN THE CLASS use __kp, aka kp WITH the double underscore, else it will run into an error.

    def PID(self, error):
        r"""
        A Proportional-Integral-Derivative algorithm for minimizing system error.
        Returns a correction signal.

        The PID algorithm is given by the formula:
            u(t) = kp*e(t) + ki*\int_{0}^{t} e(τ) \,dτ + kd*\frac{de(t)}{dt}
            u(t) = proportional_term + integral_term + derivative_term

        Where:
            u(t)    is the controller output, the correction signal the actuator
                    consumes
            e(t)    is the error value calculated as the difference between the
                    target position and the current position, in radians of
                    turret deflection for the intended use
            kp      is the proportional gain constant
            ki      is the integral gain constant
            kd      is the derivative gain constant   

        State advances on every call, so this must run at the control-loop rate
        rather than once per received measurement.

        Keyword Args:
            error -- the instantaneous error 
        """

        current_time = time.monotonic()
        dt = current_time - self.__prev_time
        self.__prev_time = current_time

        proportional_term = self.__kp * error

        # NOTE: the integral term is an accumulation over time and build up for the duration of C-UAS running
        self.__integral += error * dt
        integral_term = self.__ki * self.__integral

        # NOTE: protects against first frame error or 0 dt from low measurement fidelity
        derivative_term = (error - self.__prev_error) / dt if dt > 0 else 0
        derivative_term *= self.__kd
        self.__prev_error = error

        output_term = proportional_term + integral_term + derivative_term
        return output_term
    
    #this goes to mavlink 
