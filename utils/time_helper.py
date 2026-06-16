from datetime import (
    datetime,
    timedelta
)


def calculate_eta(
    flight_id,
    flight_list
):

    for flight in flight_list:

        if (
            flight["flight_id"]
            ==
            flight_id.strip().upper()
        ):

            depart_time = (
                datetime.strptime(
                    flight["depart_time"],
                    "%Y-%m-%d %H:%M:%S"
                )
            )

            eta = (
                depart_time
                +
                timedelta(
                    minutes=flight["duration_min"]
                )
            )

            print(
                f"-> Chuyến bay "
                f"{flight['flight_id']} "
                f"cất cánh lúc: "
                f"{flight['depart_time']}"
            )

            print(
                f"-> Thời gian hạ cánh "
                f"dự kiến (ETA): "
                f"{eta}"
            )

            return

    print(
        "Không tìm thấy chuyến bay!"
    )