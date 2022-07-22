import HRSS.HRSDK as SDK
import time


# 手臂回 Home
def robot_home(robot):
    standby_point_home = SDK.Joint(
        0, 72.000, -39.500, 0.000, -122, 0.000)  # 610

    robot.SystemCommand.set_override_ratio(25)
    robot.CoordinateCommand.set_base_number(0)
    robot.MotionCommand.ptp_axis(
        SDK.SmoothMode.Smooth.value, standby_point_home)
    while True:
        check_state = robot.MotionCommand.get_motion_state()
        time.sleep(0.3)
        if check_state == 1:
            break
    time.sleep(1)


def bow_robot(robot):
    bow_point = SDK.Joint(0.000, 60.000, -24.500, 0.000, 30.000, 0.000)
    robot.MotionCommand.ptp_axis(SDK.SmoothMode.Smooth.value, bow_point)
    time.sleep(0.1)
    while True:
        check_state = robot.MotionCommand.get_motion_state()
        if check_state == 1:
            break

    robot.SystemCommand.set_override_ratio(30)
    bow_point = SDK.Joint(30.000, 68.000, -61.500, 35.000, -122.000, 0.000)
    robot.MotionCommand.ptp_axis(SDK.SmoothMode.Smooth.value, bow_point)
    bow_point = SDK.Joint(00.000, 60.000, -24.500, 0.000, 30.000, 0.000)
    robot.MotionCommand.ptp_axis(SDK.SmoothMode.Smooth.value, bow_point)

    # 另一向
    bow_point = SDK.Joint(-50.000, 68.000, -61.500, -35.000, -122.000, 0.000)
    robot.MotionCommand.ptp_axis(SDK.SmoothMode.Smooth.value, bow_point)
    bow_point = SDK.Joint(-0.000, 60.000, -24.500, 0.000, 30.000, 0.000)
    robot.MotionCommand.ptp_axis(SDK.SmoothMode.Smooth.value, bow_point)

    time.sleep(0.1)
    while True:
        check_state = robot.MotionCommand.get_motion_state()
        if check_state == 1:
            break


if __name__ == "__main__":
    print("Robot connecting..............")

    robot = SDK.InstanceRobot()
    # robot.ConnectionCommand.find_device()

    try:
        # robot.ConnectionCommand.open_connection(ip='192.168.6.50')
        robot.ConnectionCommand.open_connection(ip='127.0.0.1')
        robot.ControlerCommand.set_operation_mode(
            SDK.OperationMode.auto_mode.value)  # 高速
        robot.ConnectionCommand.set_connection_level(1)
    except:
        print("手臂連線異常，請重新連線！")

    # 啟動回 home
    robot_home(robot)
    print("Robot connect successful..............")
    print("====================================================")

    bow_robot(robot)

    robot_home(robot)
