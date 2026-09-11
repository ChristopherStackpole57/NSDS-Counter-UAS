# Controls

Variables

    kp : proportional gain ; The KP multiplies the current error which means it is critical for the numbers to be correct as too high of an error correction will make it oscillate or overshoot. Too little of an error, obviously, does not correct the path trajectory fast enough.

    kd : derivative gain - The KD multiples the rate of change error. If too high, it becomes noise sensitive(meaning that anything that has a certain amount of inflluence on the trajectory will also influence this and it all goes to nothing). 

    ki : integral gain - The KI multiples the accumulated error over time. Best example would be the wind, where a constant wind push would be accounted for by this, as kp cannot solve this(steady state error), and kd does not have to handle this so it won't even bother.


Errors

    steady-state error : an error which is constant, it is an non-zero offset which increases as the time(t) gets clsoer and closer to infinity. ; kp without ki
    overshoot - kp will try to correct the error given, applying a proportional reply with the error, not taking into account moment and such, and so, oslides past the target. ; kp without kd 