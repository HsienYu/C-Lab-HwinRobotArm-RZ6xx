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


# 板擦 "初始" 點
def clean_start_point(robot):
    clean_start_point = SDK.Joint(-63.000, 4.000,
                                  29.800, 50.700, -87.800, -47.600)
    robot.SystemCommand.set_override_ratio(20)
    robot.CoordinateCommand.set_base_number(10)

    while True:
        robot.MotionCommand.lin_axis(
            SDK.SmoothMode.Smooth.value, 1, clean_start_point)
        if (robot.MotionCommand.get_command_count() == 0):
            break
        time.sleep(0.1)


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

    clean = CleanWord(robot_handle=robot)  # 板擦

    # 啟動回 home
    robot_home(robot)
    print("Robot connect successful..............")
    print("====================================================")

    # 清理
    print("開始擦玻璃..............")
    clean_start_point(robot)
    clean.clean_start(10)
    print("擦玻璃結束..............")
    robot_home(robot)
