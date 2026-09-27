#ifndef CONTROLS_H
#define CONTROLS_H

namespace gnc
{
    class ControlEngine
    {
    public:
        ControlEngine(double kp, double ki, double kd, double integral = 0, double prev_error = 0, double prev_time = 0);
        ControlEngine(const ControlEngine&) = delete;

        ControlEngine& operator=(const ControlEngine&) = delete;
    private:
        double kp_;
        double ki_;
        double kd_;
        double integral_;
        double prev_error_;
        double prev_time_;
    }
}

#endif