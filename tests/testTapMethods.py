#!/usr/bin/env python3

from tap_wootric.__init__ import generate_backfilled_date
from singer import utils


class TestTapTransformingMethods():

    def test_generate_backfilled_date_func(self):
        sync_start = utils.strptime_to_utc("2021-11-06 16:30:00.32")
        expected_date_for_responses = "2021-07-06T16:30:00.320000Z"
        expected_date_for_end_users = "2021-11-06T16:30:00.320000Z"

        generated_date_for_responses = generate_backfilled_date("responses", sync_start)
        generated_date_for_end_users = generate_backfilled_date("end_users", sync_start)

        assert generated_date_for_responses == expected_date_for_responses
        assert generated_date_for_end_users == expected_date_for_end_users


if __name__ == '__main__':
    TestTapTransformingMethods().test_generate_backfilled_date_func()
