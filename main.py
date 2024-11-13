from TelloDroneBuilder import TelloDroneBuilder

if __name__ == "__main__":
    try:
        TelloDroneBuilder() \
            .take_off() \
            .set_speed(50) \
            .set_velocity(20, 0, 0, 0) \
            .set_velocity(0, 20, 0, 0) \
            .set_velocity(0, 0, 20, 0) \
            .set_velocity(0, 0, 0, 30) \
            .land() \
            .disconnect()
    except Exception as e:
        print(f"Error: {e}")
        TelloDroneBuilder().emergency_stop().disconnect()
