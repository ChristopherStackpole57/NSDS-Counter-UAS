#quick note : this is in a class to make sure it is easily accessible to other functions
#and keep in mind in Py classes do not have the privacy of C++ classes. So we use the __ to create it ourselves.

from time import monotonic, time

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
            prev_time -- a seed time to use for PID calculations
        """ 

        self.__kp = kp 
        self.__ki = ki 
        self.__kd = kd
        self.__integral = integral
        self.__prev_error = prev_error
        self.__prev_time = prev_time

    ###################################################
        
    # NOTE: read only for when needed to access the values of kp, ki, kd, integral, and prev_error.
    @property
    def kp(self) : 
        return self.__kp 
    @property
    def ki(self) : 
        return self.__ki 
    @property
    def kd(self) : 
        return self.__kd 
    @property 
    def integral(self) : 
        return self.__integral
    @property
    def prev_error(self) : 
        return self.__prev_error 
    
    ###################################################

    # NOTE: to access kp, ki, or kd, you still use kp ki and kd outside the class. IN THE CLASS use __kp, aka kp WITH the doubld underscore, else it will run into an error.

    def PID(self, error):
        """
        A Proportional-Integral-Derivative algorithm for minimizing system error.
        Returns a correction signal.

        Keyword Args:
            error -- the instantaneous error 
        """

        #kp for proportional
        #ki for integral
        #kd for derivative
        current_t = time.monotonic() 
        dt = current_t - self.__prev_time 
        self.__prev_time = current_t
        proportional = self.__kp * error
        self.__integral += error * dt # = accumulated error
        derivative = (error - self.__prev_error) / dt if dt> 0 else 0 #no errors on the first frame as we filter dt ; deriv = rate of change 
        output = proportional + (self.__ki * self.__integral) + (self.__kd * derivative)
        return output 
    
    #this goes to mavlink 
    
    

