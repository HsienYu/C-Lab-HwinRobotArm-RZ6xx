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


def think(robot):
    time.sleep(1)
    robot.CoordinateCommand.set_base_number(10)
    robot.SystemCommand.set_override_ratio(15)

    think_point_first = SDK.Point(
        1047.000, 198.000, 135.500, 180.000, -62.000, -91.000)
    robot.MotionCommand.lin_pos(
        SDK.SmoothMode.Smooth.value, 1, think_point_first)

    think_point_first.x = think_point_first.x + 210
    robot.MotionCommand.lin_pos(
        SDK.SmoothMode.Smooth.value, 1, think_point_first)
    think_point_first.x = think_point_first.x - 420
    robot.MotionCommand.lin_pos(
        SDK.SmoothMode.Smooth.value, 1, think_point_first)
    think_point_first.x = think_point_first.x + 210
    robot.MotionCommand.lin_pos(
        SDK.SmoothMode.Smooth.value, 1, think_point_first)
    think_point_first.y = think_point_first.y - 210
    robot.MotionCommand.lin_pos(
        SDK.SmoothMode.Smooth.value, 1, think_point_first)
    think_point_first.y = think_point_first.y + 420
    robot.MotionCommand.lin_pos(
        SDK.SmoothMode.Smooth.value, 1, think_point_first)
    think_point_first.y = think_point_first.y - 210
    robot.MotionCommand.lin_pos(
        SDK.SmoothMode.Smooth.value, 1, think_point_first)
    time.sleep(1)
    while True:
        check_state = robot.MotionCommand.get_motion_state()
        if check_state == 1:
            break


def happy(robot):
    robot.CoordinateCommand.set_base_number(10)
    robot.SystemCommand.set_override_ratio(30)

    happy_point = SDK.Point(832.000, 351.000, 53.500,
                            180.000, -62.000, -91.000)
    robot.MotionCommand.lin_pos(SDK.SmoothMode.Smooth.value, 1, happy_point)
    happy_point = SDK.Point(832.000, 351.000, 0.000, 180.000, -62.000, -91.000)
    robot.MotionCommand.lin_pos(SDK.SmoothMode.Smooth.value, 1, happy_point)
    time.sleep(0.1)
    while True:
        check_state = robot.MotionCommand.get_motion_state()
        if check_state == 1:
            break
    happy_point = SDK.Point(832.000, 351.000, 53.500,
                            180.000, -62.000, -91.000)
    robot.MotionCommand.lin_pos(SDK.SmoothMode.Smooth.value, 1, happy_point)
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

    think(robot)

    robot_home(robot)
