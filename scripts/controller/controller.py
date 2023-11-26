def start():
    from scheduler import scheduler
    from odometry import odometry
    from config import config
    from info.info_manager import info_manager
    import timer
    odom = odometry.odometry()
    sche = scheduler.scheduler()

    # time.sleep(10*config.SLEEP_TIME)
    
    sche.start_all()

    # # test
    # info_manager.set_linear_x(0.15)
