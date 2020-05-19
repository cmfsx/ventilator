import logging
import logging.config

logger = logging.getLogger(__name__)


class Variables:
    # Pressure sensor BUS ids
    BUS_1 = 1 # first inspiratory pressure sensor
    BUS_2 = 3 # second inspiratory pressure sensor
    BUS_3 = 4 # first expiratory pressure sensor
    BUS_4 = 5 # second expiratory pressure sensor

    # Pressure sensor values
    p1 = 0      # pressure sensor 1 on inspiratory phase
    p2 = 0      # pressure sensor 2 on inspiratory phase
    p3 = 0      # pressure sensor 3 on expiratory phase
    p4 = 0      # pressure sensor 4 on expiratory phase

    # From GUI
    calib_flow_rate = -1    # flow rate used for calibration. Set by GUI
    fio2 = 0    # fio2 value
    ie = 1      # I:E ratio
    rr = 10     # respiratory rate (RR)
    vt = 500    # tidal volume (mL)
    peep = 10   # PEEP
    ps = 20     # pressure support (Ps)

    # PID controller parameters
    Kp = 10
    Ki = 1
    Kd = 1
    pid_sampling_period = 0.2

    # Flag to indicate demo setup, where P3 is from a BME680 sensor
    demo = False
